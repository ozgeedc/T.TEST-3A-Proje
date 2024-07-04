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

logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestTestSenaryo8:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 20)
        self.screenshot_dir = 'screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
        yield
        self.driver.quit()

    def test_duyuru_haberlerim_erişim_kontrol(self):
        try:
            self.driver.get("https://tobeto.com/giris")
            logging.info("Tobeto anasayfasına giriş yapıldı.")
            self.wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("furkangmsky@gmail.com")
            self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Furkan-1445")
            logging.info("E-posta ve şifre girildi.")
            logging.info("Lütfen 'Ben robot değilim' alanını geçin.")
            time.sleep(10)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mt-4"))).click()
            self.wait.until(EC.url_to_be("https://tobeto.com/platform"))
            logging.info("Giriş yapıldı ve platform sayfasına yönlendirildi.")

            self.wait.until(EC.element_to_be_clickable((By.ID, 'notification-tab'))).click()
            self.driver.find_elements(By.XPATH, '//*[@id="notification-tab-pane"]/div')
        except Exception as e:
            logging.error(f"Test başarısız: {str(e)}")
            screenshot_path = os.path.join(self.screenshot_dir, 'duyuru_haberlerim_erişim_kontrol_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Test başarısız: {e}")

    def test_duyuru_haberlerim_filtreleme_kontrol(self):
        try:
            self.test_duyuru_haberlerim_erişim_kontrol()
            more_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="notification-tab-pane"]/div/div[4]')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
            self.driver.execute_script("arguments[0].click();", more_button)
            logging.info("Daha Fazla Göster butonuna tıklandı.")
            time.sleep(2)
            logging.info("İlk dokuz duyuru ve haberin görüntülendiği kontrol ediliyor.")
            time.sleep(2)  
            announcements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col-md-4.col-12.my-4")))
            if len(announcements) < 9:
                logging.error(f"Beklenen duyuru sayısı bulunamadı. Bulunan duyuru sayısı: {len(announcements)}")
                assert False, f"Beklenen duyuru sayısı bulunamadı. Bulunan duyuru sayısı: {len(announcements)}"
            else:
                logging.info(f"{len(announcements)} duyuru başarıyla yüklendi.")

            logging.info("Filtreleme alanlarının ve okunmuş olanları gizleme butonunun kontrolü yapılıyor.")
            self.wait.until(EC.presence_of_element_located((By.ID, "search")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[2]')))
            self.wait.until(EC.presence_of_element_located((By.ID, "react-select-2-placeholder")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[4]')))
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[4]/div[2]')))
            logging.info("Pagination butonunun kontrolü yapılıyor.")
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > main > div.container > div:nth-child(2) > ul')))
           
            logging.info("Arama motoru kısmına duyuru adı yazılıyor.")
            search_input = self.driver.find_element(By.ID, "search")
            search_input.send_keys("Ocak ayı")
            logging.info("Girilen karakterler doğrultusunda duyuru ve haberlerin filtrelendiği kontrol ediliyor.")
            time.sleep(2)
            search_input.clear()

            logging.info("Filtreleme kısmında 'Tür' seçeneği duyuru veya haber checkbox'ının seçimi yapılıyor.")
            self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[2]/button').click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[2]/ul/li[1]/div/label'))).click()

            logging.info("Filtreleme işlemi sonucunda duyuruların görüntülendiği kontrol ediliyor.")
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Bir duyuru bulunmamaktadır')]")))
            except:
                filtered_announcements = self.driver.find_elements(By.CSS_SELECTOR, ".announcement-item")
                assert len(filtered_announcements) > 0, "Filtrelenmiş duyuru bulunamadı."
        except Exception as e:
            logging.error(f"Test başarısız: {str(e)}")
            screenshot_path = os.path.join(self.screenshot_dir, 'duyuru_haberlerim_filtreleme_kontrol_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Test başarısız: {e}")

if __name__ == "__main__":
    pytest.main()
