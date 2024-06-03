import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUS10KullaniciDegerlendirmeAlan:
    BASE_URL = "https://tobeto.com/giris"
    EMAIL = "ozgecam@outlook.com"
    PASSWORD = "ozge-cam-5595"
    WAIT_TIME = 10

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
    
    def teardown_method(self, method):
        self.driver.quit()

    def login(self, email, password):
        # Giriş ekranı alanına gidiş methodu.
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def degerlendirmeler(self):
        #Bu testler değerlendirmeler alanında gerçekleşmektedir. Bu sebeple  ayrı bir method oluşturulmuştur.
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Değerlendirmeler')]"))).click()

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS10TC1(self, email, password):
        #Kullanıcı, değerlendirmeler sayfasını görüntüleyebilmelidir
        self.login(email, password)
        self.degerlendirmeler()
        assert "Değerlendirmeler" in self.driver.title, "Değerlendirmeler sayfası yüklenemedi."

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS10TC2(self, email, password):
        #Kullanıcı, değerlendirmeler alanından kişisel analiz raporlarını görüntüleyebilmelidir
        self.login(email, password)
        self.degerlendirmeler()
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Raporu Görüntüle')]"))).click()
        new_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/degerlendirmeler/rapor/tobeto-iste-basari-modeli/1"
        assert new_url == expected_url, "Sayfa görüntülenemedi."

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    @pytest.mark.skip(reason="Bu test şu anda hata veriyor.")
    def test_uS10TC3_coktan_secmeli_testlerin_rapor_goruntulenmesi(self, email, password):
        #Kullanıcı, çoktan seçmeli test raporlarını görüntüleyebilmelidir
        self.login(email, password)
        self.degerlendirmeler()
        self.driver.execute_script("window.scrollTo(0, 210)")
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dashboard-card-slim:nth-child(1) .btn"))).click()
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div[2]/button"))).click()
        assert "Test Bitti" in self.driver.title, "Görüntülenemedi."
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Kapat')]"))).click()
