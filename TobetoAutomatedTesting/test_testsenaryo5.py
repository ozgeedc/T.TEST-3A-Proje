import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestTestSenaryo5:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 20)
        yield
        # Teardown
        self.driver.quit()

    def test_open_calender(self):
        self.driver.get("https://tobeto.com/giris")
        logging.info("Tobeto giriş sayfasına girildi.")
        
        # Sol alt kısmındaki takvim simgesine tıklama
        time.sleep(3)  # Sayfanın yüklenmesini bekleyin
        takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
        takvim_icon.click()
        logging.info("Takvim simgesine tıklandı.")

    def test_calendar_functionality(self):

    # Eğitim durumu check box'larının hepsini işaretleme
        time.sleep(2)  # Pop-up'ın yüklenmesini bekleyin
        self.driver.find_element(By.NAME, "eventEnded").click()
        self.driver.find_element(By.NAME, "eventContinue").click()
        self.driver.find_element(By.NAME, "eventBuyed").click()
        self.driver.find_element(By.NAME, "eventNotStarted").click()
        logging.info("Tüm eğitim durumu checkbox'ları işaretlendi.")
    
    
        # Takvimde eğitimlerin görüntülendiğini doğrulama
        time.sleep(2)  # Takvimin güncellenmesini bekleyin
        calendar_events = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[1]/div/div[2]/div[1]')))
        assert len(calendar_events) > 0, "Takvimde hiç eğitim bulunamadı."
        logging.info("Takvimde eğitimler başarıyla görüntülendi.")

        for event in calendar_events:
            event_name = event.find_element(By.CLASS_NAME, "text-truncate").text
            event_time = event.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[1]/div/div[2]/div[2]/a/div/span[1]").text
            event_instructor = event.find_element(By.CLASS_NAME, "text-truncate").text
            logging.info(f"Eğitim: {event_name}, Saat: {event_time}, Eğitmen: {event_instructor}")
    
    def test_education_search_filter_control(self):
        
        self.test_open_calender()
        education_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'search-event')))
        education_input.click()
        education_input.send_keys("Test")

        # Filtreleme sonuçlarını kontrol et
        time.sleep(3)  # Filtreleme işleminin tamamlanması için bekleyin
        filtered_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
      
        # Filtrelenmiş eğitimlerin takvimde görüntülendiğini doğrulayın
        assert len(filtered_events) > 0, "Takvimde filtrelenmiş eğitimler bulunamadı."
        logging.info(f"{len(filtered_events)} filtrelenmiş eğitim başarıyla görüntülendi.")
        
    def test_control_of_the_instructor_search_fuse(self):

        self.test_open_calender()


        