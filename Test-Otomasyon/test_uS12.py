# Generated by Selenium IDE
import pytest
from Locator.constant import *
from helpers import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Senaryo , Profil Oluştur alanında gerçekleşmektedir.
class TestUS12(): 
    #Sabit Değerler
    BASE_URL = "https://tobeto.com/giris"
    EMAİL ="ozgecam@outlook.com"
    PASSWORD ="ozgecam-pair2"
    SECOND = 45

    def setUp(self,method):
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
    
    def tearDown(self,method):
        self.driver.quit()

   # Login işlemi bir değişkenin içerisine atanmıştır.
    
    def login_Call(self, email, password):
        
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((EMAIL_NAME))).send_keys(email)
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((PASSWORD_NAME))).send_keys(password)
        iframe = WebDriverWait(self.driver, self.SECOND).until(EC.presence_of_element_located((RECAPTCHA_IFRAME)))
        self.driver.switch_to.frame(iframe)     
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((RECAPTCHA_CHECKBOX))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((LOGIN_BUTTON_LOCATOR))).click()

       

    def basla(self):
        button = WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Başla')]")))
        self.driver.execute_script("arguments[0].click();", button) # Bu Kod satırı JavaScript click() kodunu kullanarak Tıklama gerçekleştirir.
        
    # > Kullanıcı , profil bilgilerini düzenleyebileceği alanı görüntülemesi beklenir. OK
    @pytest.mark.parametrize("email, password", [(EMAİL , PASSWORD)])  
    def test_uS12TC1(self, email, password):
        self.login_Call(email, password)
        self.basla()
        assert "Platform" in self.driver.title, "Kişisel Bilgilerim sayfası yüklenemedi."
 
    # Kullanıcının , Deneyimlerini düzenleyebileceği alanın görüntülenmesi beklenir. OK
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)]) 
    def test_uS12TC2(self, email, password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Deneyimlerim\')]"))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.url_contains("profilimi-duzenle/deneyimlerim"))
        new_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/deneyimlerim"
        assert new_url == expected_url, "beklenenden farklı."
      
      
    # Eğitim Hayatım alanının görüntülenmesi 
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)])
    def test_uS12TC3(self, email, password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,'Eğitim Hayatım')]"))).click()
        new_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim"
        assert new_url == expected_url, "beklenenden farklı."


    #> Yetkinliklerim alanının görüntülenmesi
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)])
    def test_uS12TC4(self, email, password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Yetkinliklerim\')]"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim"
        assert new_window_url == expected_url, "Beklenenden farklı."
        

    #> Sertifikaları düzenleme alanının görüntülenmesi.
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)]) 
    def test_uS12TC5(self,email,password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Sertifikalarım\')]"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim"
        assert new_window_url == expected_url, "Beklenenden farklı."
        


    #> Kullanıcı sosyal medya hesaplarının düzenlenme alanının görüntülenmesi 
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)]) 
    def test_uS12TC6(self,email,password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Medya Hesaplarım\')]"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim"
        assert new_window_url == expected_url, "Beklenenden farklı."
        
      
      
    #> Kullanıcının yabancı dil bilgilerini ekleyebileceği alanın görüntülenmesi
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)])
    def test_uS12TC7(self,email,password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Yabancı Dillerim\')]"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil"
        assert new_window_url == expected_url, "Beklenenden farklı."
        
    #> Kullanıcı , şifre değişikliliği işlemleri
    @pytest.mark.parametrize("email, password", [(EMAİL,PASSWORD)])
    def test_uS12TC8(self,email,password):
        self.login_Call(email,password)
        self.basla()
        WebDriverWait(self.driver,self.SECOND).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(.,\'Ayarlar\')]"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/ayarlar"
        assert new_window_url == expected_url, "Beklenenden farklı."
        
        
      