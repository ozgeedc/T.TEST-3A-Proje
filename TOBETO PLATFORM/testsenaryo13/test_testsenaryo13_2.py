import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
from tkinter import filedialog
from time import sleep

# Test Senaryosu 13 (Kişisel Bilgilerim Kontrol)
# Case 2 : Profil Resmi Ekle Kontrolü

class TestProfilresmieklemekontrol():
    
    SECOND = 15

    def setup_method(self):
       
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris")

    def teardown_method(self):
       
        self.driver.quit()

    def test_login(self):
        
        email = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, "email")))
        email.send_keys("pair2tobeto2@gmail.com")

        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, "password")))
        passwordInput.send_keys("pair2tobeto2")

        
        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")))
        self.driver.switch_to.frame(iframe)

        
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()

       
        self.driver.switch_to.default_content()
        time.sleep(15)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        assert "Giriş Yap" in self.driver.title, "Anasayfa Görüntülemedi"
        sleep(2)
        
        nav_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/nav/div[1]/button")))
        nav_button.click()
        time.sleep(2)
        
        profil_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/button")))
        profil_button.click()
        time.sleep(2)
        
        profil_bilgileri_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[2]/div[2]/div/ul/li[1]/a")))
        profil_bilgileri_button.click()
        time.sleep(2)
       
        metin_kutusu = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div.col-12.mb-6.text-center > div.profile-photo.mx-auto > div")))
        metin_kutusu.click()
        time.sleep(2)
       
        photo_edit_buton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//button[@type='button'])[5]")))
        photo_edit_buton.click()
        time.sleep(1)
        
       
        root = tk.Tk()
        root.withdraw() 
        file_path = filedialog.askopenfilename() 

        upload_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        upload_input.send_keys(file_path)  
        time.sleep(2)
        
        

if __name__ == "__main__":
    pytest.main()