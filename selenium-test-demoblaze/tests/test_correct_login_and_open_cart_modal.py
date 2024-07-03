from pages.home_page import HomePage
from pages.welcome_page import WelcomePage
from pages.cart_page import CartPage

def test_correct_login(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    cart_page = CartPage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "STORE"
    home_page.open_login_modal()
    home_page.login("admin", "admin")
    assert welcome_page.is_login_link_invisible() == True
    assert welcome_page.is_signup_link_invisible() == True
    assert welcome_page.is_logout_link_visible() == True
    assert welcome_page.get_welcome_text() == "Welcome admin"
    home_page.open_cart_modal()
    cart_page.get_place_order_title_popup()
    assert cart_page.get_place_order_title_popup() == True
