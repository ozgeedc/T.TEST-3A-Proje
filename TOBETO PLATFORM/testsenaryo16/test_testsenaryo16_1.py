
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
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


  

# Test Senaryosu 16 (“Yetkinlik” Kontrol)
# Case 1 : Başarılı Yetkinlik Eklenmesi

class TestBasariliYetkinlikEklenmesi(): 
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
        
        yetkinliklerim_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[4]/span[2]")))
        yetkinliklerim_button.click()
        sleep(4)
        
        
        
        metin_kutusu= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#__next > div > main > section > div > div > div.col-12.col-lg-9 > div.row.mb-2 > div > div > div > div.css-hlgwow > div.css-19bb58m")))
        metin_kutusu.click() #Yetkinlik arama motoruna tıklatıyor.
        sleep(3)
        
        
                                       

        yetkinlik_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='react-select-5-option-1']")))
        yetkinlik_button.click() #Yetkinlik arama motoruna tıklatınca SQL seçiyor.
        sleep(3) 
                  
             
        save_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, " //*[@id='__next']/div/main/section/div/div/div[2]/button")))
        save_button.click()                                                                                                 
        sleep(5)
             
       
        
        
        
       
        
  
        



    
        
        
       

        
        