
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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
  

# Test Senaryosu 14 (“Deneyimlerim” Kontrol)
# Case 1 : Başarılı Deneyim Eklenmesi

class TestBasarilideneyimeklenmesi(): 
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
        time.sleep(20)
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
        
        deneyimlerim_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[1]")))
        deneyimlerim_button.click()
        sleep(1)
        
        kurumAdi= WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"corporationName",)))
        kurumAdi.send_keys("TOBETO")
        sleep(1)
        
        pozisyon = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"position",)))
        pozisyon.send_keys("YAZILIM TEST")
        sleep(1)
        
        deneyim_türü_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[3]/div/div/div/div[2]")))
        deneyim_türü_button.click()
        sleep(1)       
        deneyim_türü_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='react-select-5-option-2']")))
        deneyim_türü_button1.click()
        sleep(1)
        
        
        sektör = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/input")))
        sektör.send_keys("YAZILIM")
        sleep(1)
                
                      
        city = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//select[@name='country']")))
        city.send_keys("İstanbul")
        sleep(1)
        
        is_baslangici_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(6) .form-control",))) 
        is_baslangici_button.send_keys("2020-01-03")
        sleep(1)
        
                       
        
        is_bitisi_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[7]/div/div/input"))) 
        is_bitisi_button.click()
        sleep(1)
        is_bitisi_button1 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div/div/input"))) 
        is_bitisi_button1.send_keys("2024-02-11")
        sleep(1)
                         
         
               
        
        is_aciklamasi = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/textarea")))
        is_aciklamasi.send_keys("TOBETO")
        sleep(1)
        
        time.sleep(8)
        self.driver.execute_script("window.scrollTo(0,200);") 
       
        save_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        save_button.click()
        sleep(1)
    
        
        
        
       
        
  
        



    
        
        
       

        
        
        
        
        
   
       

 