from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser.
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page.
    page = browser.new_page()
    # Open the Playwright Python docs.
    page.goto("https://playwright.dev/python")

    #locate a link element with "Docs" text 
    docs_button = page.get_by_role('link',name="Docs")
    docs_button.click()

    browser.close()
