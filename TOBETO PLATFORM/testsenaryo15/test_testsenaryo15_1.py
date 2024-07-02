
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
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

  

# Test Senaryosu 15 (“Eğitim Hayatım” Kontrol)
# Case 1 : Başarılı Eğitim Eklenmesi

class TestBasariliEgitimEklenmesi(): 
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
        
        nav_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/nav/div[1]/button")))
        nav_button.click()
        sleep(1)
        
        profil_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/button")))
        profil_button.click()
        sleep(1)
        
              
        profil_bilgileri_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/ul/li[1]/a")))
        profil_bilgileri_button.click()
        sleep(1)
        
        eğitim_hayatim_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]")))
        eğitim_hayatim_button.click()
        sleep(1)
         
               
        eğitim_durumu_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/div/div/div/div[2]"))) 
        eğitim_durumu_button.click() 
        sleep(1)
        eğitim_durumu_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='react-select-5-option-2']"))) 
        eğitim_durumu_button1.click() 
        sleep(1)
        
        
        üniversite = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"University",)))
        üniversite.send_keys("Erzincan Üniversitesi")
        sleep(1)
        
        bölüm = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME,"Department",)))
        bölüm .send_keys("Yazılım")
        sleep(1)  
                             
        baslangic_yili_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[4]/div/div/input"))) 
        baslangic_yili_button.click() 
        baslangic_yili_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[4]")))  
        baslangic_yili_button1.click() 
        sleep(2)
        
        
        mezuniyet_yili_button = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[5]/div/div/input")))
        mezuniyet_yili_button.click()
        sleep(1)        
        mezuniyet_yili_button1 = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[8]")))
        mezuniyet_yili_button1.click()
        sleep(1)       
        
                
        time.sleep(5) 
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
        save_button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        save_button.click()
        sleep(5)
    
        
        
        
       
        




    
        
        
       

        
        
        
        
        
   
       

 