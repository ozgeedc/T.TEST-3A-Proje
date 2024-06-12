from selenium.webdriver.common.by import By

USERNAME_DATA = "ozgecam@outlook.com"
PASSWORD_DATA = "ozge-cam-5595"

USERNAME_LOCATOR = (By.NAME, "email")
PASSWORD_LOCATOR = (By.NAME, "password")
IFRAME_LOCATOR = {
    "recaptcha_iframe": (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']"),
    "recaptcha_checkbox": (By.CSS_SELECTOR, ".recaptcha-checkbox-border"),
}
LOGINBUTON_LOCATOR =(By.XPATH, "//button[@type='submit']")

# US 9  Kullanıcılar Profillerinde CV bilgilerini görüntüleyebilmeliler.
PROFILE_WIEW_LOCATOR = (By.XPATH, "//a[contains(text(),'Profilim')]")
CV_LINK_LOCATOR = (By.XPATH, "//button[@id='dropdown-basic']")
ONAYBUTON_LOCATOR = (By.CSS_SELECTOR, ".react-switch-bg")
COPYBUTON_LOCATOR = (By.CSS_SELECTOR, ".ms-3")
IN_WIEWBUTON_LOCATOR = (By.CSS_SELECTOR, ".cv-linkedin")

# US 10  Kullanıcı testleri çözebilmeli , çıkan sonuçların raporlarını görüntüleyebilmelidir.

WIEW_REPORT = (By.XPATH, "//a[contains(text(),'Değerlendirmeler')]")
REPORT_ANALIZ_LOCATOR = (By.XPATH, "//a[contains(text(),'Raporu Görüntüle')]")
REPORT_FRONT_LOCATOR = (By.XPATH, "//div[2]/div[2]/button")


# US 11 Kullanıcılar e-posta ve şifrelerini girerek sisteme giriş yapabilmelidir ve kendisine ait işte 
  # başarı modeli testini çözebilmeli ve bu test sonucunda çıkan Analiz Raporunu görütülüyebilmelidir.
 
NITELIK_LOCATOR = (By.XPATH,"(//button[@type='button'])[4]")

#US 12  Kullanıcıların :“Kişisel Bilgilerim”, “Deneyimlerim”, “Eğitim Hayatım”, “Yetkinliklerim”, “Sertifikalarım,
  #  Medya hesaplarım , “Yabancı dillerim” , “Ayarlar” alanlarının görüntülenmesi

CREAT_PROFIL_LOCATOR = (By.XPATH, "//button[contains(.,'Başla')]")
DENETIM_LOCATOR = (By.XPATH,"//span[contains(.,\'Deneyimlerim\')]")
LEARNING_WIEW = (By.XPATH,"//span[contains(.,'Eğitim Hayatım')]")
YETKINLIK_WIEW_LOCATOR = (By.XPATH,"//span[contains(.,\'Yetkinliklerim\')]")
SERTIFICA_WIEW_LOCATOR = (By.XPATH,"//span[contains(.,\'Sertifikalarım\')]")
MEDIA_ACCOUNT_LOCATOR = (By.XPATH,"//span[contains(.,\'Medya Hesaplarım\')]")
LANGUAGES_WIEW_LOCATOR = (By.XPATH,"//span[contains(.,\'Yabancı Dillerim\')]")
SETUP_LOCATOR = (By.XPATH,"//span[contains(.,\'Ayarlar\')]")