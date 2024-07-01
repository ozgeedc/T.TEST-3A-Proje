import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestTestSenaryo6:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 10)
        yield
        # Teardown
        self.driver.quit()
    
    def test_login_to_tobeto(self, email, password):
        try:
            self.driver.get("https://tobeto.com/giris")
            self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.driver.find_element(By.NAME, "email").send_keys(email)
            self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.driver.find_element(By.NAME, "password").send_keys(password)
            
            # Ben robot değilim alanı için bekleme süresi (manuel olarak geçmeniz için)
            logging.info("Lütfen 'Ben robot değilim' alanını geçin.")
            time.sleep(15)  # 30 saniye bekleme süresi
            
            self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
            self.wait.until(EC.presence_of_element_located((By.ID, "apply-tab")))
            logging.info("Login successful")
        except Exception as e:
            logging.error(f"Error during login: {e}")
            pytest.fail(f"Login test failed: {e}")

    def test_check_welcome_panel(self):
        # Check Başvurularım section
        self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
        assert "Başvurularım" in self.driver.page_source
        logging.info("Başvurularım section verified")
        # Check Eğitimlerim section
        self.wait.until(EC.presence_of_element_located((By.ID, "lessons-tab")))
        self.driver.find_element(By.ID, "lessons-tab").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")))
        assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]").text == "Agile 101"
        assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[1]").text == "Dr. Ecmel Ayral'dan Hoşgeldin Mesajı"
        assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[3]/div/div[2]/div/span[1]").text == "Eğitimlere Nasıl Katılırım?"
        assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[4]/div/div[2]/div/span[1]").text == "Herkes İçin Kodlama - 5B"
        # Öğenin görünürlüğünü sağlamak için kaydırma ve ardından tıklama
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lessons-tab-pane"]/div/div/div[2]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        
        # Check Duyuru ve Haberlerim section
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a')))
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a').click()
        self.wait.until(EC.presence_of_all_elements_located((By.ID, "notification-tab")))
        self.driver.find_element(By.ID, "notification-tab").click()
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="notification-tab-pane"]/div/div[4]'))).click()
        
        # Check Anketlerim section
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a')))
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "mySurvey-tab"))).click()  
        assert self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mySurvey-tab-pane"]/div/div/p'))).text == "Atanmış herhangi bir anketiniz bulunmamaktadır"

    def test_check_exams_section(self):
        self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
        
        # İlk tıklama için bekleme
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[2]/div")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        
        # "Raporu Görüntüle" butonunu bekle ve tıkla
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Raporu Görüntüle')]"))).click()
        
        # Öğeleri kontrol et
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Doğru')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Yanlış')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Boş')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Puan')]")
        assert len(elements) > 0

        # "Kapat" butonunu bekle ve tıkla
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Kapat')]"))
        ).click()


    def test_check_personal_area(self):
        self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-2 > .btn").click()
        elements = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[1]")
        assert len(elements) > 0
        self.driver.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-3 > .btn").click()
        elements = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/span")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".container-fluid > a > img").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-1 > .btn").click()
        elements = self.driver.find_elements(By.XPATH, "//*[@id='pills-education-tab']")
        assert len(elements) > 0
