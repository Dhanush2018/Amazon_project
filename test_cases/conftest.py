import pytest
from selenium import webdriver
from test_cases import config

@pytest.fixture(scope="module", params=["chrome"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox
    elif request.param == "Edge":
        driver = webdriver.Edge
        driver.get(config.URL)
        driver.maximize_window()
    else:
        raise ValueError("Unsupported browse!")
    yield driver
    driver.quit()

def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)