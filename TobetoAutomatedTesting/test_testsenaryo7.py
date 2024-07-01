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

class TestSenaryo7:
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

    def test_egitimlerim_paneli(self):
        
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
            
            self.wait.until(EC.element_to_be_clickable((By.ID, "lessons-tab"))).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[1]/div/div[2]/div/span[1]")))
            
            lessons = self.driver.find_elements(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div")
            assert len(lessons) <= 4, "4'ten fazla eğitim görüntüleniyor."
            logging.info("Eğitimlerim panelinde en fazla 4 eğitim görüntüleniyor.")
           
            more_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lessons-tab-pane"]/div/div/div[2]')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
            self.driver.execute_script("arguments[0].click();", more_button)
            logging.info("Daha Fazla Göster butonuna tıklandı.")
            time.sleep(2)
            all_lessons = self.driver.find_elements(By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div")
            assert len(all_lessons) > 4, "Bütün eğitimler görüntülenemiyor."
            logging.info("Kullanıcı kendisine tanımlanan bütün eğitimleri görüntüleyebiliyor.")
        except Exception as e:
            logging.error(f"Test failed: {str(e)}")
            raise

    def test_user_assigned_education_check(self):

        try:
            self.test_egitimlerim_paneli()
            # Seçmek istediğin eğitime tıkla
            education_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/button")))
            education_element.click()
            logging.info("Eğitim seçildi: Dr.Ecmel Ayral’dan Hoşgeldin Mesajı")
            # Favorilere Ekle butonuna tıkla
            favorite_button = self.wait.until(  EC.element_to_be_clickable((By.CLASS_NAME, "add-favorite")))
            favorite_button.click()
            logging.info("Favorilere Ekle butonuna tıklandı")
            # Favorilere ekleme işleminin başarılı olduğunu kontrol et
            success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wrapper-content"]/div[2]/div/div/p')))
            assert success_message.is_displayed(), "Favorilere ekleme işlemi başarısız"
            logging.info("Favorilere ekleme işlemi başarıyla gerçekleşti")
            # Kalp butonuna tıkla.
            heart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "like-button")))
            heart_button.click()
            logging.info("Kalp butonuna tıklandı")
            # Kalp butonunun kırmızı olduğunu ve beğenen kullanıcı sayısını kontrol et
            heart_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#dynamicContent > div > div.activity-detail-header > div > div.col-lg-11.col-md-11.col-sm-10.col-xs-12 > div > div:nth-child(1) > div > div.activity-process.col-lg-5.col-md-5.col-sm-8.col-xs-12.text-lg-right.text-md-right.text-sm-right.text-xs-center > div > div:nth-child(3) > div > div > span.like-button.liked')))
            assert heart_icon.is_displayed(), "Kalp butonu kırmızıya dönüşmedi"
            logging.info("Kalp butonu kırmızıya dönüştü")
            # Hakkında butonuna tıkla
            about_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-0-tab-about"]')))
            about_button.click()
            logging.info("Hakkında butonuna tıklandı")
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper-content"]/div[2]/div')))
            # İçerik butonuna tıkla
            content_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-0-tab-content"]' )))
            content_button.click()
            logging.info("İçerik butonuna tıklandı")
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="rc-tabs-0-panel-content"]/div')))
            # Detay butonuna tıkla
            detail_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activity-unit-detail"]/div/div[2]/div/div/div[2]/button')))
            detail_button.click()
            logging.info("Detay butonuna tıklandı")
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/div')))
            # Detay sayfasında “Eğitime Git” butonuna tıkla.
            go_to_educaiton_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div[1]/div/div[1]/a')))
            go_to_educaiton_button.click()
            logging.info("Eğitime Git butonuna tıklandı")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rc-tabs-0-panel-content"]/div')))
            # Detay butonuna tıkla
            detail_button.click()
            logging.info("Detay butonuna tekrar tıklandı")
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/div')))
            # Detay sayfasında “X” butonuna tıkla.
            close_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/a')))
            close_button.click()
            logging.info("Detay sayfasında X butonuna tıklandı")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rc-tabs-0-panel-content"]/div')))
        except Exception as e:
            logging.error(f"Test failed: {str(e)}")
            raise
            
    def test_training_completion(self):
        try:  
            self.test_egitimlerim_paneli()
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="all-lessons-tab-pane"]/div/div[15]/div/div[2]/button')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            logging.info("Eğitim seçildi: Softskill: İletişim Becerileri")

            video_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "video")))
            self.driver.execute_script("arguments[0].play()", video_element)
            logging.info("Video oynatılıyor: Softskill: İletişim Becerileri")
            time.sleep(120)
            
            tamamladin_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dynamicContent"]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div')))   
            assert tamamladin_text.is_displayed(), "Tamamladın yazısı bulunamadı"
            logging.info("Eğitim başlığının altında 'Tamamladın' yazısı görüntülendi")

            progress_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dynamicContent"]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div')))
            assert progress_bar.is_displayed(), "İlerleme çubuğunda % 100 yazısı bulunamadı"
            logging.info("İlerleme çubuğunda % 100 yazısı görüntülendi")

            tebrikler_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="activity-unit-detail"]/div/div[1]/div[3]')))
            assert tebrikler_text.is_displayed(), "Tebrikler, tamamladın! yazısı bulunamadı"
            logging.info("Videonun altında 'Tebrikler, tamamladın!' yazısı görüntülendi")

            detail_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activity-unit-detail"]/div/div[2]/div/div/div[2]/button')))
            detail_button.click()
            logging.info("Detay butonuna tıklandı")
            detail_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div[2]/span')))
            assert detail_page.is_displayed(), "Detay sayfasında Tebrikler, tamamladın! yazısı bulunamadı"
            logging.info("Detay sayfasında 'Tebrikler, tamamladın!' yazısı görüntülendi")
        except Exception as e:
          logging.error(f"Test failed: {str(e)}")
          raise

    def test_search_in_lessons(self):
        try:
            self.test_egitimlerim_paneli()
            search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]')))
            search_box.click()
            logging.info("Arama kutucuğuna tıklandı")
            
            search_box.send_keys("Dr. Ecmel Ayral'dan Hoşgeldin Mesajı")
            filtered_education = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="all-lessons-tab-pane"]/div/div/div/div[2]/div')))
            assert filtered_education.is_displayed(), "Arama sonucu doğru eğitim bulunamadı."
            logging.info("Arama sonucu doğru eğitim bulundu: Dr.Ecmel Ayral’dan Hoşgeldin Mesajı")
            
            institution_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]')))
            self.driver.execute_script("arguments[0].click();", institution_box)
            institution_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select__input-container > input")))
            institution_input.send_keys("İst")
            logging.info("Arama sonucu doğru kurum bulundu: İstanbul Kodluyor")
        except Exception as e:
            logging.error(f"Test failed: {str(e)}")
            raise

    def test_sorting_in_lessons(self):
        try:
            self.test_egitimlerim_paneli()
    
            # Adım 6: Sıralama kutusuna tıklama
            sorting_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-3-input"]')))
            sorting_box.click()
            logging.info("Sıralama kutusuna tıklandı")
    
            # Adım 7: Sıralama türlerini seçme ve kontrol etme
            sorting_types = {
                "Adına Göre (A-Z)": '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[3]/div/div/div[1]/div[1]',
                "Adına Göre (Z-A)": '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[3]/div/div/div[1]/div[1]',
                "Tarihe Göre (Y-E)": '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[3]/div/div/div[1]/div[1]',
                "Tarihe Göre (E-Y)": '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[3]/div/div/div[1]/div[1]'
            }
    
            for sorting_type, xpath in sorting_types.items():
                sorting_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                self.driver.execute_script("arguments[0].click();", sorting_option)
                logging.info(f"Sıralama türü seçildi: {sorting_type}")
                
                sorted_lessons = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div/div[3]/div/div/div[1]/div[1]')
                assert len(sorted_lessons) > 0, f"Sıralama türü doğru uygulanmadı: {sorting_type}"
                logging.info(f"Sıralama türü doğru uygulandı: {sorting_type}")
    
        except Exception as e:
            logging.error(f"Test failed: {str(e)}")
            raise
        