# Generated by Selenium IDE
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.by import By as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUS10Kullancdeerlendirmealan():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
    
  
  def teardown_method(self, method):
    self.driver.quit()

  #Kullanıcı , değerlendirmeler sayfasını görüntüleyebilmelidir. OK

  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS10TC1(self,email, password,):
    
    WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)

    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type=\'submit\']")))
    girisYap = self.driver.find_element(By.XPATH,"//button[@type=\'submit\']")
    girisYap.click()

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")))
    degerlendirme = self.driver.find_element(By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")
    degerlendirme.click()
    assert "Değerlendirmeler" in self.driver.title, "Değerlendirmeler sayfası yüklenemedi." #Değerlendirmeler başlığının karşılaştırmasını yapar.




    # Kullanıcı Değerlendirmeler alanından , kişisel analiz raporlarını görüntüleyebilmesi beklenir. OK

  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS10TC2(self, email, password):
    WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type=\'submit\']")))
    girisYap = self.driver.find_element(By.XPATH,"//button[@type=\'submit\']")
    girisYap.click()

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")))
    degerlendirme = self.driver.find_element(By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")
    degerlendirme.click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'Raporu Görüntüle\')]")))
    raporgoruntuleme = self.driver.find_element(By.XPATH, "//a[contains(text(),\'Raporu Görüntüle\')]")
    raporgoruntuleme.click()
     # Sayfa içeriğini doğrula , Link karşılaştırması sayfa içerikleri ve başlıkları çakıştığından link olarak düzenlenmiştir.
    new_url = self.driver.current_url
    expected_url = "https://tobeto.com/profilim/degerlendirmeler/rapor/tobeto-iste-basari-modeli/1"
    assert new_url == expected_url, "Sayfa görüntülenemedi."

    #Çoktan seçemeli test raporlarının görüntülenmesi beklenir. BU KISIM HATA VERMEKTEDİR.
   
  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS10TC3oktanSemeliTestlerinRaporGrntlenmesi(self, email, password):
    WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type=\'submit\']")))
    girisYap = self.driver.find_element(By.XPATH,"//button[@type=\'submit\']")
    girisYap.click()

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")))
    degerlendirme = self.driver.find_element(By.XPATH, "//a[contains(text(),\'Değerlendirmeler\')]")
    degerlendirme.click()

    self.driver.execute_script("window.scrollTo(0,210)")

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "//button[contains(.,'Raporu Görüntüle')]")))
    buton = self.driver.find_element(By.XPATH, "//button[contains(.,'Raporu Görüntüle')]")   #HATA vermektedir.
    buton.click()

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[2]/div[2]/button")))
    raporgoruntule = self.driver.find_element(By.XPATH, "//div[2]/div[2]/button")
    raporgoruntule.click()
    assert "Test Bitti" in self.driver.title, "Görüntülenemedi." #Değerlendirmeler başlığının karşılaştırmasını yapar.
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Kapat\')]")))
    closebutton = self.driver.find_element(By.XPATH, "//button[contains(.,\'Kapat\')]")
    closebutton.click()
   
  