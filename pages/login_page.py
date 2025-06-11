from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"

    def open(self):
        self.driver.get(self.url)

    def fill_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def is_login_button_visible(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed()

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_flash_message(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        flash_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        return flash_element.text.strip()

    def is_logout_button_visible(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "a.button.secondary.radius")) > 0

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()
