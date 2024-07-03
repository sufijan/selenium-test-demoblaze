from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def go_to(self):
        self.selenium_webdriver.get("https://www.demoblaze.com")
        self.selenium_webdriver.maximize_window()

    def get_page_tile(self):
        return self.selenium_webdriver.title
    
    def open_login_modal(self):
        login_link_locator = (By.ID, "login2")
        wait_login_link = self.wait.until(EC.element_to_be_clickable(login_link_locator))
        wait_login_link.click()

    def login(self, username, password):
        username_field_locator = (By.ID, "loginusername")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_webdriver.find_element(By.ID, "loginpassword")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_webdriver.find_element(By.XPATH, "//button[text()=\"Log in\"]")
        login_button.click()
    
    def is_alert_window_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False
        
    def get_alert_window_message(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text
    
    def open_cart_modal(self):
        cart_link_locator = (By.ID, "cartur")
        cart_link = self.wait.until(EC.element_to_be_clickable(cart_link_locator))
        cart_link.click()