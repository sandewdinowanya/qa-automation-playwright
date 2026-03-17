from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser.
    browser = playwright.chromium.launch(headless=False)
    # Create a new page.
    page = browser.new_page()
    # Open the Playwright Python docs.
    page.goto("https://playwright.dev/python")

    browser.close()
