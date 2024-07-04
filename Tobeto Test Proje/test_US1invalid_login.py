import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
from constants import globalConstants as c

class TestInvalidLogin:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(c.LOGIN_URL)
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
        
#Test Senaryosu 1 Adı : Giriş Paneli Kontrolü
#Case 3 :  E-posta veya Şifre Hatalı Girildiğinde

    @pytest.mark.parametrize("email, password", [
        ("invalid@gmai.com", "pair2tobeto2"),
        ("pair2tobeto2@gmail.com", "12"),
        ("invalid@gmai.com", "12")
    ])
    def test_invalid_login(self, email, password):
        self.login(email, password)
        self.check_login_unsuccessful()

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

        iframe = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, c.IFRAME_LOGIN_CSS)))
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, c.CAPTCHA_LOGIN_CSS))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, c.LOGIN_BUTTON_XPATH))).click()

    def check_login_unsuccessful(self):
        toast_locator = (By.CLASS_NAME, "toast-body")
        try:
            toast = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(toast_locator))
            assert toast.text == "• Geçersiz e-posta veya şifre."
        except TimeoutException:
            raise AssertionError("Login unsuccessful message not displayed.")
        sleep(3)
