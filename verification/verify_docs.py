from playwright.sync_api import sync_playwright

def verify_docs(page):
    page.goto("http://localhost:8000/index.html")

    # 1. Hero Variants
    # Locate the Hero Variants section. It has a header "Hero Variants".
    # The code block should be after the component-demo.
    hero_section = page.locator("h2:has-text('Hero Variants')").locator("..").locator("..")
    # Scroll into view
    hero_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/docs_hero.png", clip=hero_section.bounding_box())

    # 2. Avatar
    avatar_section = page.locator("h2:has-text('Avatar Component')").locator("..").locator("..")
    avatar_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/docs_avatar.png", clip=avatar_section.bounding_box())

    # 3. Join
    join_section = page.locator("h2:has-text('Join Component')").locator("..").locator("..")
    join_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/docs_join.png", clip=join_section.bounding_box())

    # 4. Tooltips & Loading
    tooltip_section = page.locator("h2:has-text('Tooltips & Loading')").locator("..").locator("..")
    tooltip_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/docs_tooltip.png", clip=tooltip_section.bounding_box())

    # 5. Toast
    toast_section = page.locator("h2:has-text('Toast Component')").locator("..").locator("..")
    toast_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path="verification/docs_toast.png", clip=toast_section.bounding_box())

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})
        verify_docs(page)
        browser.close()
