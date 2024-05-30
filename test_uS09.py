# Generated by Selenium IDE
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUS09Profilbilgilerinigrntlmesibeklenir():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
    #self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

   # Kullanıcı profil bilgilerinin güncellenmesi ve görüntülenmesi
  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS9TC1(self, email, password):
   
    WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)
    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type=\'submit\']")))
    girisYap = self.driver.find_element(By.XPATH,"//button[@type=\'submit\']")
    girisYap.click()

    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),\'Profilim\')]")))
    ProfilimButon = self.driver.find_element(By.XPATH, "//a[contains(text(),\'Profilim\')]")
    ProfilimButon.click()

   # Kullanıcı , Tobeto sitesinden Profil bilgilerini paylaşabilmelidir. URL Kopyalandı bilgisi alması beklenir.

  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS9TC2(self, email, password):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
    login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Profilim')]")))
    profil_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Profilim')]")
    profil_button.click()
   
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id='dropdown-basic']")))
    profilipaylas = self.driver.find_element(By.XPATH, "//button[@id='dropdown-basic']")
    profilipaylas.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".react-switch-bg")))
    switch = self.driver.find_element(By.CSS_SELECTOR, ".react-switch-bg")
    
    switch.click()
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".ms-3")))
    copybuton = self.driver.find_element(By.CSS_SELECTOR, ".ms-3")
    copybuton.click()
    expected_message = "• Url kopyalandı." #Beklenen hata sonucu
    actual_message = self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text#Hata sonucunu içerisine alır
    assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}" #Çıkan sonuçları karşılaştırı
    testResult = expected_message=="• Url kopyalandı."
    print(f"TEST SONUCU: {testResult}")
   
  # Kullanıcı , Profilim alanından sertifikalarını indirebilmelidir.
  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS9TC3SertifikaKontrolveDosyannindirilmesibeklenir(self, email, password):
    self.driver.get("https://tobeto.com/giris")
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
    login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Profilim')]")))
    profil_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Profilim')]")
    profil_button.click()

    self.driver.execute_script("window.scrollTo(0,1000)") # Ekran görüntüsü ekle .. 
    #self.vars["window_handles"] = self.driver.window_handles
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ".cursor-pointer:nth-child(1) > .d-flex")))
    self.driver.find_element(By.XPATH, ".cursor-pointer:nth-child(1) > .d-flex").click()
    #self.vars["C:\Users\Busraa\Downloads"] = self.wait_for_window(2000)
    #self.vars["root"] = self.driver.current_window_handle
    #self.driver.switch_to.window(${C:\\Users\\Busraa\\Downloads})
    

  # Kullanıcı , sosyal medya hesaplarına tıkladığında sosyal medya hesaplarına yönlendirilmeli ve görüntülenmesi beklenir.
  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")])
  def test_uS9TC4(self, email, password):
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
    login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Profilim')]")))
    profil_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Profilim')]")
    profil_button.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cv-linkedin")))
    linkedinbuton = self.driver.find_element(By.CSS_SELECTOR, ".cv-linkedin")
    linkedinbuton.click()
    new_window_url = self.driver.current_url
    expected_url = "https://www.linkedin.com/in/ozgeedc1610"
    assert new_window_url == expected_url, "LinkedIn URL'si beklenenden farklı."

    

  # İşte Başarım , Analiz Raporu Görüntülenmelidir.
  @pytest.mark.parametrize("email, password", [("ozgecam@outlook.com", "ozge-cam-5595")]) 
  def test_uS9TC5(self, email, password):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"email")))
    username = self.driver.find_element(By.NAME,"email")
    username.send_keys(email)
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,"password")))
    password_field = self.driver.find_element(By.NAME,"password")
    password_field.send_keys(password) 
    
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
    login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")
    login_button.click()

    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Profilim')]")))
    profil_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Profilim')]")
    profil_button.click()
    self.driver.execute_script("window.scrollTo(0,300)")

    assert EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Tobeto İşte Başarı Modelim')]"))
    #Sayfada Tobeto İşte Başarı Modelim alanı görünüyor mu görünmüyor mu diye kontrol eder .
    
  
