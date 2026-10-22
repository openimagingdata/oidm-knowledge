import { h } from "preact"
import { readFileSync } from "node:fs"
import { fileURLToPath } from "node:url"
import { parse } from "yaml"
import { pathToRoot, resolveRelative, simplifySlug, slugifyFilePath } from "@quartz-community/utils/path"

const css = readFileSync(new URL("./style.css", import.meta.url), "utf8")
const navigationFile = process.env.SITE_NAVIGATION_FILE || fileURLToPath(new URL("../../../../navigation.yaml", import.meta.url))
// Read once at build time. Optional labels override parsed page titles.
const navigation = parse(readFileSync(navigationFile, "utf8"))
const slugFor = (page) => slugifyFilePath(page)
const samePage = (left, right) => simplifySlug(left) === simplifySlug(right)

export const ReviewBanner = () => {
  const Component = () => process.env.SITE_TARGET === "production" ? null :
    h("div", { class: "review-banner", role: "note", "aria-label": "Review status" }, "DRAFT / Awaiting Review")
  Component.css = css
  return Component
}

export const SiteLogo = () => {
  const Component = ({ fileData }) => {
    const root = pathToRoot(fileData.slug)
    return h("div", { class: "site-logo" },
      h("a", { href: root, class: "internal", "aria-label": "Open Imaging Data Model: Knowledge home" },
        h("img", { class: "site-logo-light", src: `${root}/static/brand/logo-color.svg`, alt: "Open Imaging Data Model", width: 208 }),
        h("img", { class: "site-logo-dark", src: `${root}/static/brand/logo-white.svg`, alt: "Open Imaging Data Model", width: 208 }),
        h("span", { class: "site-logo-caption" }, "Knowledge")))
  }
  Component.css = css
  return Component
}

const chevron = () => h("svg", { class: "site-nav-chevron", width: 16, height: 16, viewBox: "0 0 16 16", "aria-hidden": "true" },
  h("path", { d: "m6 4 4 4-4 4", fill: "none", stroke: "currentColor", "stroke-width": 1.5, "stroke-linecap": "round", "stroke-linejoin": "round" }))

export const SiteNav = () => {
  const Component = ({ fileData, allFiles }) => {
    const pages = new Map(allFiles.map((file) => [file.slug, file]))
    const pageFor = (item) => typeof item === "string" ? item : item.page
    const labelFor = (item) => (typeof item === "string" ? undefined : item.label) ?? pages.get(slugFor(pageFor(item)))?.frontmatter?.title
    const link = (item, child = false) => {
      const page = pageFor(item)
      const slug = slugFor(page)
      const title = pages.get(slug)?.frontmatter?.title
      if (!title) throw new Error(`navigation.yaml: no parsed title for ${page}`)
      const active = samePage(fileData.slug, slug)
      return h("a", {
        href: resolveRelative(fileData.slug, slug),
        class: `internal site-nav-link${child ? " site-nav-child" : ""}`,
        "aria-current": active ? "page" : undefined,
        "data-nav-slug": simplifySlug(slug),
      }, labelFor(item))
    }
    const entry = (item) => {
      const page = pageFor(item)
      const children = typeof item === "string" ? [] : item.pages || []
      if (!children.length) return h("li", { class: "site-nav-pillar", key: page }, link(item))
      const current = [page, ...children].some((child) => samePage(fileData.slug, slugFor(typeof child === "string" ? child : child.page)))
      return h("li", { class: "site-nav-pillar", key: page },
        h("details", { class: "site-nav-section", open: current, "data-nav-pillar": simplifySlug(slugFor(page)) },
          h("summary", { "aria-label": `Toggle ${labelFor(item)} pages` }, link(item), chevron()),
          h("ul", { class: "site-nav-children" }, children.map((child) => h("li", { key: pageFor(child) }, link(child, true))))))
    }
    return h("nav", { class: "site-nav", "aria-label": "Site contents" },
      // Separate desktop and phone shells keep the phone panel closed with
      // native details even when JavaScript is disabled. CSS shows one shell.
      h("div", { class: "site-nav-desktop" }, h("ul", { class: "site-nav-list" }, navigation.map(entry))),
      h("details", { class: "site-nav-mobile" },
        h("summary", null, h("span", null, "Contents"), chevron()),
        h("ul", { class: "site-nav-list" }, navigation.map(entry))))
  }
  Component.css = css
  // micromorph preserves the user's details.open property. Reconcile only
  // on real page navigation so the current pillar follows the new page.
  Component.afterDOMLoaded = `
document.addEventListener("nav", function(event) {
  var slug = (event.detail.url || "").replace(/\\/index$/, "/");
  if (slug === "index" || slug === "") slug = "/";
  document.querySelectorAll(".site-nav").forEach(function(nav) {
    nav.querySelectorAll("a[data-nav-slug]").forEach(function(link) {
      if (link.dataset.navSlug === slug) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
    });
    nav.querySelectorAll(".site-nav-section").forEach(function(section) {
      section.open = !!section.querySelector('[aria-current="page"]');
    });
    nav.querySelectorAll(".site-nav-mobile").forEach(function(panel) { panel.open = false; });
  });
});
`
  return Component
}

// The pinned v5 layout loader chooses one export per source entry. The
// adapter lets three YAML entries use their own options and positions.
export const SiteChrome = (options) => {
  const constructors = { ReviewBanner, SiteLogo, SiteNav }
  const constructor = constructors[options?.component]
  if (!constructor) return () => null
  return constructor()
}
