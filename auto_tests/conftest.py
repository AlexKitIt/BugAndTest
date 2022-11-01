import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()
    yield browser

    browser.quit()
