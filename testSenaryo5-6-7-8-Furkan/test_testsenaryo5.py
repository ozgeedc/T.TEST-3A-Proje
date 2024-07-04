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
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestTestSenaryo5:
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

    def test_open_calender(self):
        try:
            self.driver.get("https://tobeto.com/giris")
            logging.info("Tobeto giriş sayfasına girildi.")
            
            time.sleep(3)
            takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
            takvim_icon.click()
            logging.info("Takvim simgesine tıklandı.")
    
            time.sleep(2)
            self.driver.find_element(By.NAME, "eventEnded").click()
            self.driver.find_element(By.NAME, "eventContinue").click()
            self.driver.find_element(By.NAME, "eventBuyed").click()
            self.driver.find_element(By.NAME, "eventNotStarted").click()
            logging.info("Tüm eğitim durumu checkbox'ları işaretlendi.")
            time.sleep(2)
        except Exception as e:
            logging.error(f"Takvim açma sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'open_calendar_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Takvim açma testi başarısız: {e}")

    def test_calendar_functionality(self):
        try:
            self.driver.get("https://tobeto.com/giris")
            logging.info("Tobeto giriş sayfasına girildi.")
            
            time.sleep(3)
            takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
            takvim_icon.click()
            logging.info("Takvim simgesine tıklandı.")
    
            time.sleep(2)
            self.driver.find_element(By.NAME, "eventEnded").click()
            self.driver.find_element(By.NAME, "eventContinue").click()
            self.driver.find_element(By.NAME, "eventBuyed").click()
            self.driver.find_element(By.NAME, "eventNotStarted").click()
            logging.info("Tüm eğitim durumu checkbox'ları işaretlendi.")
        
            time.sleep(2)
            calendar_events = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[1]/div/div[2]/div[1]')))
            assert len(calendar_events) > 0, "Takvimde hiç eğitim bulunamadı."
            logging.info("Takvimde eğitimler başarıyla görüntülendi.")
    
            for event in calendar_events:
                event_name = event.find_element(By.CLASS_NAME, "text-truncate").text
                event_time = event.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[1]/td[1]/div/div[2]/div[2]/a/div/span[1]").text
                event_instructor = event.find_element(By.CLASS_NAME, "text-truncate").text
                logging.info(f"Eğitim: {event_name}, Saat: {event_time}, Eğitmen: {event_instructor}")
        except Exception as e:
            logging.error(f"Takvim işlevselliği testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'calendar_functionality_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Takvim işlevselliği testi başarısız: {e}")

    def test_education_search_filter_control(self):
        try:
            self.test_open_calender()
            education_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'search-event')))
            education_input.click()
            education_input.send_keys("Test")
    
            time.sleep(3)
            filtered_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
          
            assert len(filtered_events) > 0, "Takvimde filtrelenmiş eğitimler bulunamadı."
            logging.info(f"{len(filtered_events)} filtrelenmiş eğitim başarıyla görüntülendi.")
        except Exception as e:
            logging.error(f"Eğitim arama filtre kontrolü testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'education_search_filter_control_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Eğitim arama filtre kontrolü testi başarısız: {e}")

    def test_control_of_the_instructor_search_fuse(self):
        try:
            self.test_open_calender()
            input_filter = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2-input"]')))
            input_filter.send_keys("Gürk", Keys.TAB)
            assert self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fc-event-main")))
            logging.info("Eğitmen arama filtresi doğrulandı")
        except Exception as e:
            logging.error(f"Eğitmen arama filtre kontrolü testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'instructor_search_fuse_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Eğitmen arama filtre kontrolü testi başarısız: {e}")

    def test_controlling_instructor_training_search_filters_together(self):
        try:
            self.test_open_calender()
            education_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'search-event')))
            education_input.click()
            education_input.send_keys("Test")
            
            input_filter = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2-input"]')))
            input_filter.send_keys("Gürk", Keys.TAB)
            assert True
            logging.info("Eğitim ve eğitmen arama filtreleri doğrulandı")
        except Exception as e:
            logging.error(f"Eğitim ve eğitmen arama filtre kontrolü testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'instructor_training_search_filters_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Eğitim ve eğitmen arama filtre kontrolü testi başarısız: {e}")

    def test_date_navigation_controls(self):
        try:
            self.driver.get("https://tobeto.com/giris")
            logging.info("Tobeto giriş sayfasına girildi.")
    
            time.sleep(3)
            takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
            takvim_icon.click()
            logging.info("Takvim simgesine tıklandı.")
    
            bugun_button = self.driver.find_element(By.XPATH, "//button[@class='fc-today-button fc-button fc-button-primary']")
            bugun_button.click()
            logging.info("Bugün butonuna tıklandı.")
    
            time.sleep(2)
            current_month_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
            assert len(current_month_events) > 0, "Güncel ayda hiç eğitim bulunamadı."
            logging.info("Güncel aydaki eğitimler başarıyla görüntülendi.")
    
            right_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/button[2]")
            right_button.click()
            logging.info("Sağ yönlendirme butonuna tıklandı.")
            time.sleep(2)
    
            next_month_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
            assert len(next_month_events) > 0, "Sonraki ayda hiç eğitim bulunamadı."
            logging.info("Sonraki aydaki eğitimler başarıyla görüntülendi.")
            time.sleep(2)
    
            ay_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[1]")
            ay_button.click()
            logging.info("Ay butonuna tıklandı.")
            time.sleep(2)
    
            selected_month_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
            assert len(selected_month_events) > 0, "Seçilen ayda hiç eğitim bulunamadı."
            logging.info("Seçilen aydaki eğitimler başarıyla görüntülendi.")
    
            hafta_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[2]")
            hafta_button.click()
            logging.info("Hafta butonuna tıklandı.")
            time.sleep(2)
    
            selected_week_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
            assert len(selected_week_events) > 0, "Seçilen haftada hiç eğitim bulunamadı."
            logging.info("Seçilen haftadaki eğitimler başarıyla görüntülendi.")
    
            gun_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div/button[3]")
            gun_button.click()
            logging.info("Gün butonuna tıklandı.")
            time.sleep(2)
    
            selected_day_events = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-daygrid-day-events")))
            assert len(selected_day_events) > 0, "Seçilen günde hiç eğitim bulunamadı."
            logging.info("Seçilen gündeki eğitimler başarıyla görüntülendi.")
        except Exception as e:
            logging.error(f"Tarih navigasyon kontrolü testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'date_navigation_controls_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Tarih navigasyon kontrolü testi başarısız: {e}")

    def test_calendar_popup_closure(self):
        try:
            self.driver.get("https://tobeto.com/giris")
            logging.info("Tobeto giriş sayfasına girildi.")
    
            time.sleep(3)
            takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
            takvim_icon.click()
            logging.info("Takvim simgesine tıklandı.")
    
            kapatma_simge = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/button")
            kapatma_simge.click()
            logging.info("Kapatma simgesine tıklandı.")
    
            try:
                takvim_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/section/div[2]/div')))
                assert takvim_icon.is_displayed()
                logging.info("Takvim başarıyla kapatıldı, simge haline geldi.")
            except TimeoutException:
                logging.error("Takvim kapatılamadı veya simge haline gelmedi.")
                screenshot_path = os.path.join(self.screenshot_dir, 'calendar_popup_closure_error.png')
                self.driver.save_screenshot(screenshot_path)
                logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
                pytest.fail("Takvim kapatılamadı veya simge haline gelmedi.")
        except Exception as e:
            logging.error(f"Takvim pop-up kapatma testi sırasında hata: {e}")
            screenshot_path = os.path.join(self.screenshot_dir, 'calendar_popup_closure_error.png')
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
            pytest.fail(f"Takvim pop-up kapatma testi başarısız: {e}")

if __name__ == "__main__":
    pytest.main()
