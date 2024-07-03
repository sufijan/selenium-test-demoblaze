from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)
    
    def get_place_order_title_popup(self):
        signup_link_locator = (By.ID, "orderModalLabel")
        try:
            self.wait.until(EC.invisibility_of_element_located(signup_link_locator))
            return True
        except TimeoutException:
            return False

    
        