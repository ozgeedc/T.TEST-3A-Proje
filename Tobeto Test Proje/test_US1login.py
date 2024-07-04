import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from time import sleep
from constants import globalConstants as c

#Test Senaryosu 1 Adı : Giriş Paneli Kontrolü

class Test_Login:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(c.LOGIN_URL)
        self.login("pair2tobeto2@gmail.com", "pair2tobeto2")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()


#Case 1 : Başarılı Giriş Kontrolü
    
    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, c.IFRAME_LOGIN_CSS)))
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, c.CAPTCHA_LOGIN_CSS))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, c.LOGIN_BUTTON_XPATH))).click()

    def wait_and_click(self, by, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()

    def wait_for_elements(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))
    
    def test_login_success(self):
        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(toast_locator))
        assert toast.text == "• Giriş başarılı."
        sleep(3)
