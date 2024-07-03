from pages.home_page import HomePage

def test_incorrect_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.get_page_tile() == "STORE"
    home_page.open_login_modal()
    home_page.login("wrong username", "wrong password")
    assert home_page.is_alert_window_present() == True
    assert home_page.get_alert_window_message() == "User does not exist."