from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_username("tomsmith")
    login_page.fill_password("SuperSecretPassword!")
    login_page.click_login()

    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert login_page.is_logout_button_visible()

    login_page.click_logout()


def test_login_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_username("invalidUser")
    login_page.fill_password("invalidPass")
    login_page.click_login()

    assert "Your username is invalid!" in login_page.get_flash_message()


def test_login_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login()

    assert "Your username is invalid!" in login_page.get_flash_message()

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_username("tomsmith")
    login_page.fill_password("SuperSecretPassword!")
    login_page.click_login()

    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert login_page.is_logout_button_visible()

    login_page.click_logout()

    assert login_page.is_login_button_visible()
    assert "You logged out of the secure area!" in login_page.get_flash_message()
