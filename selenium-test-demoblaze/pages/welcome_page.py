from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WelcomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)
    
    def is_login_link_invisible(self):
        login_link_locator = (By.ID, "login2")
        try:
            self.wait.until(EC.invisibility_of_element_located(login_link_locator))
            return True
        except TimeoutException:
            return False
    
    def is_signup_link_invisible(self):
        signup_link_locator = (By.ID, "signin2")
        try:
            self.wait.until(EC.invisibility_of_element_located(signup_link_locator))
            return True
        except TimeoutException:
            return False
    
    def is_logout_link_visible(self):
        logout_link_locator = (By.ID, "logout2")
        try:
            self.wait.until(EC.element_to_be_clickable(logout_link_locator))
            return True
        except TimeoutException:
            return False
    
    def get_welcome_text(self):
        welcome_text_locator = (By.ID, "nameofuser")
        wait_welcome_text = self.wait.until(EC.element_to_be_clickable(welcome_text_locator))
        return wait_welcome_text.text