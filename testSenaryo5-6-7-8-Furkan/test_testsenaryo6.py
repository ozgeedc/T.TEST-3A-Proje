import pytest
import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestTestSenaryo6:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 10)
        self.screenshot_dir = 'screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
        yield
        self.driver.quit()
    
    def test_login_to_tobeto(self, email, password):
        try:
            self.driver.get("https://tobeto.com/giris")
            self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.driver.find_element(By.NAME, "email").send_keys(email)
            self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.driver.find_element(By.NAME, "password").send_keys(password)
            logging.info("Lütfen 'Ben robot değilim' alanını geçin.")
            time.sleep(10)  
            self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
            self.wait.until(EC.presence_of_element_located((By.ID, "apply-tab")))
            logging.info("Giriş başarılı")
        except Exception as e:
            logging.error(f"Giriş sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'login_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Giriş testi başarısız: {e}")

    def test_check_welcome_panel(self):
        try:
            self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
            assert "Başvurularım" in self.driver.page_source
            logging.info("Başvurularım bölümü doğrulandı")
            self.wait.until(EC.presence_of_element_located((By.ID, "lessons-tab")))
            self.driver.find_element(By.ID, "lessons-tab").click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")))
            assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]").text == "Agile 101"
            assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/div/span[1]").text == "Dr. Ecmel Ayral'dan Hoşgeldin Mesajı"
            assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[3]/div/div[2]/div/span[1]").text == "Eğitimlere Nasıl Katılırım?"
            assert self.driver.find_element(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[4]/div/div[2]/div/span[1]").text == "Herkes İçin Kodlama - 5B"
            logging.info("Dersler doğrulandı")
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lessons-tab-pane"]/div/div/div[2]')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            logging.info("Belirli bir derse yönlendirildi")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a')))
            self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a').click()
            logging.info("Ana menüye gidildi")
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "notification-tab")))
            self.driver.find_element(By.ID, "notification-tab").click()
            self.driver.execute_script("window.scrollTo(0, 400)")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="notification-tab-pane"]/div/div[4]'))).click()
            logging.info("Bildirimlere tıklandı")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a')))
            self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a').click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "mySurvey-tab"))).click()
            assert self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mySurvey-tab-pane"]/div/div/p'))).text == "Atanmış herhangi bir anketiniz bulunmamaktadır"
            logging.info("Anket sekmesi doğrulandı")
        except Exception as e:
            logging.error(f"Test başarısız: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'welcome_panel_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            raise

    def test_check_exams_section(self):
        try:
            self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
            logging.info("Giriş başarılı")
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[2]/div")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            logging.info("Belirli bir bölüme gidildi")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Raporu Görüntüle')]"))).click()
            logging.info("Rapor görüntülendi")
            elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Doğru')]")
            assert len(elements) > 0
            logging.info("'Doğru' elements doğrulandı")
            elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Yanlış')]")
            assert len(elements) > 0
            logging.info("'Yanlış' elements doğrulandı")
            elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Boş')]")
            assert len(elements) > 0
            logging.info("'Boş' elements doğrulandı")
            elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Puan')]")
            assert len(elements) > 0
            logging.info("'Puan' elements doğrulandı")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Kapat')]"))).click()
            logging.info("Rapor kapatıldı")
        except Exception as e:
            logging.error(f"Test başarısız: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'exams_section_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            raise

    def test_check_personal_area(self):
        try:
            self.test_login_to_tobeto("furkangmsky@gmail.com", "Furkan-1445")
            logging.info("Giriş başarılı")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            logging.info("Sayfa sonuna kaydırıldı")
            
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-2 > .btn").click()
            logging.info("İlk butona tıklandı")
        
            elements = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[1]")
            assert len(elements) > 0
            logging.info("İlk bölümde elemanlar bulundu")
            self.driver.find_element(By.XPATH, "//*[@id='__next']/div/nav/div[1]/a").click()
            logging.info("İlk navigasyon linkine tıklandı")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            logging.info("Sayfa sonuna kaydırıldı")
            self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-3 > .btn").click()
            logging.info("İkinci butona tıklandı")
            elements = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/span")
            assert len(elements) > 0
            logging.info("İkinci bölümde elemanlar bulundu")
            self.driver.find_element(By.CSS_SELECTOR, ".container-fluid > a > img").click()
            logging.info("Ana sayfa linkine tıklandı")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            logging.info("Sayfa sonuna kaydırıldı")
            self.driver.find_element(By.CSS_SELECTOR, ".pack-bg-1 > .btn").click()
            logging.info("Üçüncü butona tıklandı")
            elements = self.driver.find_elements(By.XPATH, "//*[@id='pills-education-tab']")
            assert len(elements) > 0
            logging.info("Eğitim sekmesi bulundu")
        except Exception as e:
            logging.error(f"Test başarısız: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'personal_area_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            raise

if __name__ == "__main__":
    pytest.main()
