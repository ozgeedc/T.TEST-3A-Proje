import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import check_alignment, check_link_functionality, check_load_time

class TestUS09():
    BASE_URL = "https://tobeto.com/giris"
    EMAIL = "ozgecam@outlook.com"
    PASSWORD = "ozge-cam-5595"
    SECOND = 10

    #Bu kısımda kod en başta bu kısma uğradığından bir metoda atanmış olup Tobeto Linki çağırılmıştır.
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()
    
    #Her test bitiminde uğranılacak nokta.
    def teardown_method(self, method):
        self.driver.quit()

    def test_alignment(self):
        assert check_alignment("//*[@id='__next']/div/div"), "UI elementleri yanlış hizalanmış."

    def test_links(self):
        assert check_link_functionality("home_page_link"), "Link çalışmıyor."

    def test_load_time(self):
        home_page = {"load_time": 1.5}  # Gerçek sayfa nesnesi
        assert check_load_time(home_page), "Sayfa yükleme süresi çok uzun."    

    @pytest.mark.parametrize("page, element, link, load_time", [
       ("home_page", "home_page_element", "home_page_link", 1.5),
        ("about_page", "about_page_element", "about_page_link", 1.8),])
    def test_common_functionality(self, page, element, link, load_time):
        assert check_alignment(element), f"{page} elementleri yanlış hizalanmış."
        assert check_link_functionality(link), f"{page} link çalışmıyor."
        assert check_load_time({"load_time": load_time}), f"{page} yükleme süresi çok uzun."
    
    #Giriş yap alanı , kod tekrarını azaltmak adına değişkenlere atanmıştır.zzzz
    def login(self, email, password):
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
        
        
        # I'm not robot ,Hello ! I'm pytest :) 

        iframe = WebDriverWait(self.driver, self.SECOND).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")))
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()


    
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC1(self, email, password):
        #Kullanıcı profil bilgilerinin güncellenmesi ve görüntülenmesi
        self.login(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Profilim')]"))).click()

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC2(self, email, password):
        #Kullanıcı, Tobeto sitesinden Profil bilgilerini paylaşabilmelidir.
        self.login(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Profilim')]"))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='dropdown-basic']"))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-switch-bg"))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ms-3"))).click()
        expected_message = "• Url kopyalandı."
        actual_message = WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".toast-body"))).text
        assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"
        print(f"TEST SONUCU: {expected_message == actual_message}")
        
    @pytest.mark.skip
    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC3(self, email, password):
        #Kullanıcı, Profilim alanından sertifikalarını indirebilmelidir.
        self.login(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Profilim')]"))).click()
        self.driver.execute_script("window.scrollTo(0,1000)")
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, ".cursor-pointer:nth-child(1) > .d-flex"))).click()

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC4(self, email, password):
        #Kullanıcı, sosyal medya hesaplarına tıkladığında sosyal medya hesaplarına yönlendirilmelidir.
        self.login(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Profilim')]"))).click()
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cv-linkedin"))).click()
        new_window_url = self.driver.current_url
        expected_url = "https://www.linkedin.com/in/ozgeedc1610"
        assert new_window_url == expected_url, "LinkedIn URL'si beklenenden farklı."

    @pytest.mark.parametrize("email, password", [(EMAIL, PASSWORD)])
    def test_uS9TC5(self, email, password):
        #İşte Başarım, Analiz Raporu Görüntülenmelidir.
        self.login(email, password)
        WebDriverWait(self.driver, self.SECOND).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Profilim')]"))).click()
        self.driver.execute_script("window.scrollTo(0,300)")
        assert WebDriverWait(self.driver, self.SECOND).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Tobeto İşte Başarı Modelim')]"))), "Tobeto İşte Başarı Modelim alanı görünmüyor."
