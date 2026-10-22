// Lightbox: click-to-zoom image viewer for article diagrams.
//
// This is a component-only Quartz plugin: the component itself renders
// nothing (Quartz still mounts it so its .css and .beforeDOMLoaded get
// collected into every page - see componentResources.ts in Quartz core).
// All behavior lives in the beforeDOMLoaded script below.
//
// This is beforeDOMLoaded, not afterDOMLoaded, deliberately: in a production
// build Quartz code-splits every component's afterDOMLoaded script into its
// own hashed file, all loaded in parallel via dynamic import() and only
// awaited as a group before the SPA router itself initializes (see
// componentResources.ts). That leaves a real window, right after page load
// under real network latency, where a user can click a diagram before our
// chunk has loaded and registered its click interceptor - the click then
// falls through to Quartz's SPA router uncontested, which tries to fetch the
// .svg as an html page and does a background window.location.assign(),
// silently navigating away. beforeDOMLoaded scripts are always bundled into
// one single, blocking prescript.js loaded synchronously in <head> before
// the body is even parsed, so registering the interceptor there guarantees
// it exists before anything on the page is clickable at all. The overlay
// DOM itself is still built lazily, on first real open() call - safe, since
// a real click implies the body has already rendered.

const css = `
.site-lightbox {
  position: fixed;
  inset: 0;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  /* Always a dark scrim, independent of site theme: --light/--dark are
     foreground/background ROLE tokens that swap literal colors between
     light and dark mode (in dark mode --dark is a near-white text color),
     so using either for a dimming backdrop would invert in dark mode. */
  background: rgba(10, 10, 12, 0.92);
  backdrop-filter: blur(2px);
}
.site-lightbox[hidden] {
  display: none;
}
.site-lightbox-stage {
  flex: 1 1 auto;
  position: relative;
  overflow: hidden;
  cursor: grab;
  touch-action: none;
}
.site-lightbox-stage:active {
  cursor: grabbing;
}
.site-lightbox-img {
  position: absolute;
  left: 0;
  top: 0;
  margin: 0;
  max-width: none;
  max-height: none;
  width: auto;
  height: auto;
  transform-origin: 0 0;
  will-change: transform;
  background: var(--light);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
  touch-action: none;
  user-select: none;
  -webkit-user-drag: none;
}
.site-lightbox-toolbar {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  padding: 0.75rem;
}
.site-lightbox-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 2.25rem;
  height: 2.25rem;
  padding: 0 0.75rem;
  border-radius: 6px;
  border: 1px solid var(--lightgray);
  background: var(--light);
  color: var(--dark);
  font-family: inherit;
  font-size: 0.95rem;
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
}
.site-lightbox-btn:hover {
  background: var(--lightgray);
}
.site-lightbox-btn:focus-visible {
  outline: 2px solid var(--secondary);
  outline-offset: 2px;
}
.site-lightbox-close {
  font-size: 1.3rem;
}
.site-lightbox-hint {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0.5rem 0.75rem;
  text-align: center;
  font-size: 0.75rem;
  color: var(--gray);
  pointer-events: none;
}
body.site-lightbox-lock {
  overflow: hidden;
}
`

const script = `
function siteLightboxBuild() {
  var overlay = document.createElement("div")
  overlay.className = "site-lightbox"
  overlay.setAttribute("role", "dialog")
  overlay.setAttribute("aria-modal", "true")
  overlay.setAttribute("aria-label", "Image viewer")
  overlay.hidden = true

  var stage = document.createElement("div")
  stage.className = "site-lightbox-stage"

  var img = document.createElement("img")
  img.className = "site-lightbox-img"
  img.alt = ""
  img.draggable = false
  stage.appendChild(img)

  var toolbar = document.createElement("div")
  toolbar.className = "site-lightbox-toolbar"

  function mkButton(label, ariaLabel, extraClass) {
    var b = document.createElement("button")
    b.type = "button"
    b.className = "site-lightbox-btn" + (extraClass ? " " + extraClass : "")
    b.textContent = label
    b.setAttribute("aria-label", ariaLabel)
    return b
  }

  var openFull = document.createElement("a")
  openFull.className = "site-lightbox-btn"
  openFull.textContent = "Open full size"
  openFull.target = "_blank"
  openFull.rel = "noopener noreferrer"

  var zoomOutBtn = mkButton("−", "Zoom out")
  var resetBtn = mkButton("Reset", "Reset zoom")
  var zoomInBtn = mkButton("+", "Zoom in")
  var closeBtn = mkButton("×", "Close image viewer", "site-lightbox-close")

  toolbar.appendChild(openFull)
  toolbar.appendChild(zoomOutBtn)
  toolbar.appendChild(resetBtn)
  toolbar.appendChild(zoomInBtn)
  toolbar.appendChild(closeBtn)

  var hint = document.createElement("div")
  hint.className = "site-lightbox-hint"
  hint.textContent = "Scroll to zoom · drag to pan · double-click to reset · Esc to close"

  overlay.appendChild(stage)
  overlay.appendChild(toolbar)
  overlay.appendChild(hint)
  document.body.appendChild(overlay)

  var scale = 1, tx = 0, ty = 0
  var naturalW = 0, naturalH = 0
  var triggerEl = null
  var inlineWidthPx = 0
  var MIN_SCALE = 0.1, MAX_SCALE = 20
  var TOP_MARGIN = 16

  function applyTransform() {
    img.style.transform = "translate(" + tx + "px," + ty + "px) scale(" + scale + ")"
  }

  // Fits the image to the viewport WIDTH only, not literal 1:1 - height is
  // deliberately not part of this calculation. These diagrams are portrait
  // (taller than wide) while browser viewports are landscape, so a fit that
  // also constrains height is almost always height-bound and ends up
  // *narrower* than the already-squeezed inline rendering, defeating the
  // point of clicking in. Height overflow is normal here: the stage is
  // pannable (drag, or pinch/wheel-zoom recentering), and opens scrolled to
  // the top of the diagram rather than vertically centered, so the reader
  // lands where the diagram starts. Floored at the inline rendered scale so
  // this can never make the image look smaller than what was just clicked -
  // that floor is measured once, when the click that opened this image
  // happened, and reused for Reset/double-click within this same open().
  // The true 1:1 resolution is reachable via wheel/pinch zoom or the "Open
  // full size" button, which bypasses the overlay entirely.
  function fitAndCenter() {
    var rect = stage.getBoundingClientRect()
    var widthFit = naturalW > 0 && rect.width > 0 ? (0.92 * rect.width) / naturalW : 1
    var inlineFit = inlineWidthPx > 0 && naturalW > 0 ? inlineWidthPx / naturalW : 0
    scale = Math.max(widthFit, inlineFit)
    tx = (rect.width - naturalW * scale) / 2
    ty = TOP_MARGIN
    applyTransform()
  }

  function zoomAt(clientX, clientY, factor) {
    var rect = stage.getBoundingClientRect()
    var mx = clientX - rect.left
    var my = clientY - rect.top
    var imgX = (mx - tx) / scale
    var imgY = (my - ty) / scale
    var next = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale * factor))
    tx = mx - imgX * next
    ty = my - imgY * next
    scale = next
    applyTransform()
  }

  function focusables() {
    return [openFull, zoomOutBtn, resetBtn, zoomInBtn, closeBtn]
  }

  // An <img> pointing at an SVG that has a viewBox but no width/height
  // attribute (the case for every diagram in this bundle) reports a
  // naturalWidth/Height from the CSS default-object-size fallback (~300px
  // wide), not the SVG's real authored resolution - so "full size" would
  // actually be smaller than the squeezed inline rendering. Fetch and parse
  // the SVG's own width/height or viewBox to get the true intrinsic size;
  // fall back to the <img>'s reported natural size for anything else.
  function resolveSize(src, cb) {
    var isSvg = /\.svg(?:[?#]|$)/i.test(src)
    if (!isSvg) {
      cb(img.naturalWidth || img.width, img.naturalHeight || img.height)
      return
    }
    fetch(src)
      .then(function (res) {
        return res.text()
      })
      .then(function (text) {
        var doc = new DOMParser().parseFromString(text, "image/svg+xml")
        var root = doc.documentElement
        var w = root && root.getAttribute("width")
        var h = root && root.getAttribute("height")
        if (w && h && !/%/.test(w) && !/%/.test(h)) {
          cb(parseFloat(w), parseFloat(h))
          return
        }
        var vb = root && root.viewBox && root.viewBox.baseVal
        if (vb && vb.width && vb.height) {
          cb(vb.width, vb.height)
          return
        }
        cb(img.naturalWidth || img.width, img.naturalHeight || img.height)
      })
      .catch(function () {
        cb(img.naturalWidth || img.width, img.naturalHeight || img.height)
      })
  }

  function open(src, alt, trigger, inlineWidth) {
    triggerEl = trigger || null
    inlineWidthPx = inlineWidth || 0
    img.src = src
    img.alt = alt || ""
    overlay.setAttribute("aria-label", alt ? "Image viewer: " + alt : "Image viewer")
    openFull.href = src
    overlay.hidden = false
    document.body.classList.add("site-lightbox-lock")

    resolveSize(src, function (w, h) {
      naturalW = w
      naturalH = h
      img.style.width = naturalW + "px"
      img.style.height = naturalH + "px"
      fitAndCenter()
    })

    closeBtn.focus()
  }

  function close() {
    if (overlay.hidden) return
    overlay.hidden = true
    document.body.classList.remove("site-lightbox-lock")
    img.removeAttribute("src")
    if (triggerEl && typeof triggerEl.focus === "function") triggerEl.focus()
    triggerEl = null
  }

  overlay.addEventListener("click", function (e) {
    if (e.target === overlay || e.target === stage || e.target === hint) close()
  })
  closeBtn.addEventListener("click", close)
  resetBtn.addEventListener("click", fitAndCenter)
  openFull.addEventListener("click", function (e) {
    e.stopPropagation()
  })
  zoomInBtn.addEventListener("click", function () {
    var r = stage.getBoundingClientRect()
    zoomAt(r.left + r.width / 2, r.top + r.height / 2, 1.4)
  })
  zoomOutBtn.addEventListener("click", function () {
    var r = stage.getBoundingClientRect()
    zoomAt(r.left + r.width / 2, r.top + r.height / 2, 1 / 1.4)
  })

  stage.addEventListener(
    "wheel",
    function (e) {
      if (overlay.hidden) return
      e.preventDefault()
      var factor = e.deltaY < 0 ? 1.15 : 1 / 1.15
      zoomAt(e.clientX, e.clientY, factor)
    },
    { passive: false },
  )

  img.addEventListener("dblclick", function (e) {
    e.preventDefault()
    fitAndCenter()
  })

  // Pointer-based pan (mouse/touch/pen) with two-finger pinch-to-zoom.
  var pointers = new Map()
  var dragStart = null
  var pinchStart = null

  function dist(a, b) {
    return Math.hypot(a.x - b.x, a.y - b.y)
  }
  function midpoint(a, b) {
    return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 }
  }

  img.addEventListener("pointerdown", function (e) {
    img.setPointerCapture(e.pointerId)
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY })
    if (pointers.size === 1) {
      dragStart = { x: e.clientX, y: e.clientY, tx: tx, ty: ty }
      pinchStart = null
    } else if (pointers.size === 2) {
      dragStart = null
      var pts = Array.from(pointers.values())
      pinchStart = { dist: dist(pts[0], pts[1]), mid: midpoint(pts[0], pts[1]), scale: scale, tx: tx, ty: ty }
    }
  })

  img.addEventListener("pointermove", function (e) {
    if (!pointers.has(e.pointerId)) return
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY })
    if (pointers.size === 1 && dragStart) {
      tx = dragStart.tx + (e.clientX - dragStart.x)
      ty = dragStart.ty + (e.clientY - dragStart.y)
      applyTransform()
    } else if (pointers.size === 2 && pinchStart) {
      var pts = Array.from(pointers.values())
      var d = dist(pts[0], pts[1])
      var factor = d / pinchStart.dist
      var rect = stage.getBoundingClientRect()
      var mx = pinchStart.mid.x - rect.left
      var my = pinchStart.mid.y - rect.top
      var imgX = (mx - pinchStart.tx) / pinchStart.scale
      var imgY = (my - pinchStart.ty) / pinchStart.scale
      var next = Math.min(MAX_SCALE, Math.max(MIN_SCALE, pinchStart.scale * factor))
      tx = mx - imgX * next
      ty = my - imgY * next
      scale = next
      applyTransform()
    }
  })

  function endPointer(e) {
    pointers.delete(e.pointerId)
    if (pointers.size === 0) {
      dragStart = null
      pinchStart = null
    } else if (pointers.size === 1) {
      var p = Array.from(pointers.values())[0]
      dragStart = { x: p.x, y: p.y, tx: tx, ty: ty }
      pinchStart = null
    }
  }
  img.addEventListener("pointerup", endPointer)
  img.addEventListener("pointercancel", endPointer)

  document.addEventListener("keydown", function (e) {
    if (overlay.hidden) return
    if (e.key === "Escape") {
      close()
      return
    }
    if (e.key === "Tab") {
      var items = focusables()
      var first = items[0]
      var last = items[items.length - 1]
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault()
        last.focus()
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault()
        first.focus()
      }
    }
  })

  return { overlay: overlay, open: open, close: close }
}

// The overlay is built lazily, on the first real open() call, not eagerly
// here - this whole script runs once, synchronously, before document.body
// exists (see the comment above), so nothing here can touch document.body.
var lightbox = null

// Open on click of any article image (or its wrapping link). Registered on
// document in the capture phase, in beforeDOMLoaded, so it is guaranteed to
// exist before Quartz's SPA router's bubble-phase click listener on window
// can ever see a click - see the file-level comment for why that ordering
// matters. stopPropagation keeps a matched click from ever reaching that
// listener; modifier-clicks (new tab / new window) and middle-click are left
// alone so the plain link still works as a fallback.
document.addEventListener(
  "click",
  function (e) {
    if (e.button !== 0 || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return
    var targetImg = e.target && e.target.closest && e.target.closest("article img")
    if (!targetImg) return
    var link = targetImg.closest("a")
    var src = link ? link.href : targetImg.currentSrc || targetImg.src
    if (!src) return
    var inlineWidth = targetImg.getBoundingClientRect().width || 0
    e.preventDefault()
    e.stopPropagation()
    if (!lightbox) lightbox = siteLightboxBuild()
    lightbox.open(src, targetImg.alt, link || targetImg, inlineWidth)
  },
  true,
)

// Quartz's SPA router (micromorph) diffs document.body against the freshly
// fetched page and strips elements - like our dynamically-appended overlay -
// that aren't part of it, so re-append (and defensively close) on every nav.
document.addEventListener("nav", function () {
  if (!lightbox) return
  if (!document.body.contains(lightbox.overlay)) {
    document.body.appendChild(lightbox.overlay)
  }
  lightbox.close()
})
`

const LightboxConstructor = (_userOpts) => {
  const Lightbox = () => null
  Lightbox.css = css
  Lightbox.beforeDOMLoaded = script
  return Lightbox
}

export { LightboxConstructor as Lightbox }
