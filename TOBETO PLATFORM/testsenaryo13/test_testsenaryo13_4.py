
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Test Senaryosu 13 (Kişisel Bilgilerim Kontrol)
# Case 4 : “TC Kimlik No“ Boş Bırakma Kontrolü

class TestTcbosbirakma(): 
    SECOND = 15

    def setup_method(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris")

    def teardown_method(self):
        
        self.driver.quit()

    def test_login(self):
       
        email = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME, "email")))
        email.send_keys("pair2tobeto2@gmail.com")

        passwordInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME, "password")))
        passwordInput.send_keys("pair2tobeto2")

      
        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")))
        self.driver.switch_to.frame(iframe)

        
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()

        
        self.driver.switch_to.default_content()
        time.sleep(15)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        assert "Giriş Yap" in self.driver.title, "Anasayfa Görüntülemedi"
        time.sleep(5)
        
        nav_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/nav/div[1]/button")))
        nav_button.click()
        sleep(1)
        
        profil_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/button")))
        profil_button.click()
        sleep(1)
        
              
        profil_bilgileri_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/ul/li[1]/a")))
        profil_bilgileri_button.click()
        sleep(1)
        
        
        
        name = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"name",)))
        name.clear()
        name.send_keys("Demet")
        sleep(1)
        
        surname = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"surname",)))
        surname.clear()
        surname.send_keys("Koç")
        sleep(1)
        
                
        phoneNumber = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"phoneNumber",)))
        phoneNumber.clear()
        phoneNumber.send_keys("555 665 26 55")
        sleep(1)
        
        birthday = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(5) > .form-control",)))
        birthday.send_keys("12-12-1990")
        sleep(1)
        
        
        identifier = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input")))
        identifier.send_keys()
        sleep(1)
        
        time.sleep(5)  # Sayfanın yüklenmesi için 2 saniye bekle
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        
        save_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        save_button.click()
        sleep(5)
        
       
       
        
        
       
  
  
        



   
    
        
        
       

        
        
        
        
        
   
       

 