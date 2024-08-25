from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(browser, delay_seconds=10, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        EC.presence_of_element_located((by, value))
    )


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = wait_element(browser, by=By.CSS_SELECTOR, value="#login_link")
    login_link.click()
