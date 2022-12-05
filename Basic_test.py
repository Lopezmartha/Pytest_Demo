from playwright.sync_api import Page

def test_example(page: Page):
    page.goto("https://www.exploratorytestingacademy.com/app/")
    page.fill("#inputtext", "Software tester're detailed oriented")
    page.click("#CheckForEPrimeButton")
    assert page.inner_text("#wordCount") == "5"
    assert page.inner_text("#discouragedWordCount") == "1"
    assert page.inner_text("#possibleViolationCount") == "0"
    #page.click("#/html/body/div/div[1]/p[2]/a")