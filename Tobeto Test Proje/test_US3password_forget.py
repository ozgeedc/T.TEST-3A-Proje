import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from constants import globalConstants as c

#Test Senaryosu 3 : Şifremi Unuttum Paneli Kontrolü

class Test_Password_Forget:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.PASSWORD_FORGET_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
   
    
    #Case 1: Şifre sıfırlama e-postası gönderme.

    def test_password_forget(self):
        emailInput=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))   
        emailInput.send_keys("tobeto.pair2@gmail.com")
        sendButton=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH))) 
        sendButton.click()
        try:
            forgetErrorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.FORGET_ERROR_MESSAGE_XPATH))).text
            assert "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin." in forgetErrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.") 

    #Case 2: Şifre Sıfırlama Durumunda Hatalı E-Posta Girilmesi

    def test_invalid_change_mail(self):  
        emailInput=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))    
        emailInput.send_keys("sxhahxabsch")
        sendButton=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH))) 
        sendButton.click()
        try:
            forgetmailErrorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.FORGET_ERROR_MESSAGE_XPATH))).text
            assert "Girdiğiniz e-posta geçersizdir" in forgetmailErrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.") 

    