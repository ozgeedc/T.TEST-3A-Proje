import os
import pytest
import allure
from helpers import *
from Locator.constant import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class TestUS09():
    
    EMAIL = "ozgecam@outlook.com"
    PASSWORD = "ozge-cam-5595"
    SECOND = 15

    #Bu kısımda kod en başta bu kısma uğradığından bir metoda atanmış olup Tobeto Linki çağırılmıştır.
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
    
    #Her test bitiminde uğranılacak nokta.
    def teardown_method(self, method):
        self.driver.quit()

    
    def login_Call(self, email, password):
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((EMAIL_NAME))).send_keys(email)
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((PASSWORD_NAME))).send_keys(password)
        
        # I'm not robot ,Hello ! I'm pytest :) 

        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((RECAPTCHA_IFRAME)))
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((RECAPTCHA_CHECKBOX))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((LOGIN_BUTTON_LOCATOR))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((PROFILE_VIEW_LOCATOR))).click()
        
    @allure.title("Kullanıcı profil bilgilerinin görüntülenmesi")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC1(self, email, password):
        #Kullanıcı profil bilgilerinin güncellenmesi ve görüntülenmesi
        self.login_Call(email, password)
        assert "Platform" in self.driver.title, "Profile page not loaded successfully"

    @allure.title("Tobeto sitesinde profil bilgilerini paylaşma")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC2(self, email, password):
        self.login_Call(email, password)
        cvlink = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(CV_LINK_LOCATOR))
        cvlink.click()
        onaybutton = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(APPROVAL_BUTTON_LOCATOR))
        onaybutton.click()
        copyB = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(COPY_BUTTON_LOCATOR))
        copyB.click()
        success_message = WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((URL_COPY_TEXT))).text
        assert "Url kopyalandı." in success_message, "Error sharing profile information"
        
    
    @allure.title("Kullanıcı, Profilim alanından sertifikalarını indirebilmelidir")   
    @pytest.mark.skip
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)]) # araştır
    def test_uS9TC3(self, email, password):
        
        self.login_Call(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, ".cursor-pointer:nth-child(1).>.d-flex"))).click()
         # Sertifika indirme işlemini gerçekleştirin
        download_button = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'İndir')]")))
        download_button.click()
      # İndirilen dosyanın mevcut olup olmadığını kontrol edin
        downloaded_file_path = "/path/to/downloaded/file"  # İndirilen dosyanın yolu
        assert os.path.exists(downloaded_file_path), "Certificate download failed"


    @allure.title("Kullanıcı, sosyal medya hesaplarına tıkladığında sosyal medya hesaplarına yönlendirilmelidir")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC4(self, email, password):
        self.login_Call(email, password)
        linkedin_button = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(LINKEDIN_VIEW_LOCATOR))
        linkedin_button.click()
        open_url = self.driver.current_url
        expected_url = "https://www.linkedin.com/in/ozgeedc1610"
        assert open_url == expected_url, "LinkedIn görüntülenemedi."

    @allure.title("İşte Başarım, Analiz Raporu Görüntülenmelidir")
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC5(self, email, password):
        self.login_Call_TEST(email, password)   
        tobeto_model = WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable(TOBETO_MODEL_LOCATOR))
        assert tobeto_model, "Tobeto İşte Başarı Modelim alanı görünmüyor."

    