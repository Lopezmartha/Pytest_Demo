import pytest
from playwright.sync_api import Page

url = "https://www.exploratorytestingacademy.com/app/"

def this_is_sample(): 
    with open('sample_b1.txt') as f:
        lines = f.readlines()
    return str(lines)

data = [
    
    (this_is_sample(), 151, 10, 0), 
    ("The little girl is cute", "5", "1", "0"),
    ("We're going home", "3", "0", "0"),
    ("You're looking good", "3", "0", "0"),
    ("ten\ntwenty", "1", "0", "0"),
    ("<div>hey</div>", "1", "0", "0"),
    ("HelloPython"*1000, "1", "0", "0"),
    ("cat"*1000 , "1", "0", "0"),
    
]


@pytest.mark.parametrize('input_text, expect_wordcount, expect_discouraged, expect_violation', data)
def test_parametrized_test(page: Page, input_text, expect_wordcount, expect_discouraged, expect_violation):
    page.goto(url)
    page.fill("#inputtext", input_text)
    page.click("#CheckForEPrimeButton")
    assert page.inner_text("#wordCount") == str(expect_wordcount)
    assert page.inner_text("#discouragedWordCount") == str(expect_discouraged)
    assert page.inner_text("#possibleViolationCount") == str(expect_violation)