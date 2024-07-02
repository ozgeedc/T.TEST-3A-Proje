
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
# Case 3 : TC Kimlik No Hatalı Girme

class TestTckimlikhataligirme(): 
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
        time.sleep(2)
      
        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")))
        self.driver.switch_to.frame(iframe)

        
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()

        
        self.driver.switch_to.default_content()
        time.sleep(20)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        assert "Giriş Yap" in self.driver.title, "Anasayfa Görüntülemedi"
        time.sleep(5)
        
        nav_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/nav/div[1]/button")))
        nav_button.click()
        time.sleep(2)
        
        profil_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/button")))
        profil_button.click()
        time.sleep(2)
        
              
        profil_bilgileri_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/ul/li[1]/a")))
        profil_bilgileri_button.click()
        time.sleep(2)
        
               
        name = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"name",)))
        name.clear()
        name.send_keys("Demet")
        time.sleep(2)
        
        surname = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"surname",)))
        surname.clear()
        surname.send_keys("Koç")
        time.sleep(2)
        
                
        phoneNumber = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"phoneNumber",)))
        phoneNumber.clear()
        phoneNumber.send_keys("555 665 26 55")
        time.sleep(2)
        
        birthday = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(5) > .form-control",)))
        birthday.send_keys("12-12-1990")
        time.sleep(2)
        
        identifier = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"identifier",)))
        identifier.send_keys("444444444444444")
        time.sleep(2)
        
        
        self.driver.execute_script("window.scrollTo(0,300);") 
        time.sleep(3)
         
       
    
        
        cinsiyet_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/div/div/div/div[2]")))
        cinsiyet_button.click()
        time.sleep(2)
        cinsiyet_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='react-select-2-option-1']")))
        cinsiyet_button1.click()
        time.sleep(3)
    
        askerlik_button1 = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[9]/div/div/div[1]/div[2]/input")))
        askerlik_button1.click()    
        time.sleep(3)
         
      
       
        
        engellilik_durumu_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/div/div/div/div[2]")))
        engellilik_durumu_button.click()
        engellilik_durumu_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='react-select-4-option-1']")))
        engellilik_durumu_button1.click()
        time.sleep(2)
        
        github_adresi = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, "githubAddress")))
        github_adresi.send_keys(".")
        time.sleep(2)
        
        ülke = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, "country")))
        ülke.send_keys("Türkiye")
        time.sleep(2)
        
        il_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, "city")))
        il_button.send_keys("İstanbul")
        time.sleep(2)
        
        ilçe_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, "district")))
        ilçe_button.send_keys("Avcılar")
        time.sleep(2)
        
        self.driver.execute_script("window.scrollTo(0,850);") 
        time.sleep(3)
        
        address = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"address")))
        address.send_keys("Murat Mah. Sancar Sok.")
        time.sleep(2)
        
        about_us = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(16) > .form-control")))
        about_us.send_keys("Yazılım Test mühendisliği alanında Tobeto da eğitim alıyorum.")
        time.sleep(2) 
        
        
        
        
        save_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        save_button.click()
        time.sleep(2)
        
       

        
        
        
       
  
        



  
        
        
       

        
        
        
        
        
   
       

 