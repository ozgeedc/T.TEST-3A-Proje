from selenium.webdriver.common.by import By




BASE_URL = "https://tobeto.com/giris"
#EMAIL = "ozgecam@outlook.com"
#PASSWORD = "ozge-cam-5595"
SECOND = 10
# Locatorlar
EMAIL_NAME = (By.NAME, "email")
PASSWORD_NAME = (By.NAME, "password")
RECAPTCHA_IFRAME = (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']")
RECAPTCHA_CHECKBOX= (By.CSS_SELECTOR, ".recaptcha-checkbox-border")
LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")

# Profil ve CV görüntüleme locatorları
PROFILE_VIEW_LOCATOR = (By.XPATH, "//a[contains(text(),'Profilim')]")
CV_LINK_LOCATOR = (By.XPATH, "//button[@id='dropdown-basic']")
APPROVAL_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".react-switch-bg")
COPY_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".ms-3")
LINKEDIN_VIEW_LOCATOR = (By.CSS_SELECTOR, ".cv-linkedin")
URL_COPY_TEXT = (By.CSS_SELECTOR, ".toast-body")
PROFILE_URL = "https://tobeto.com/profilim"
TEST_BITTI = (By.CSS_SELECTOR,"body > div.fade.modal.show > div > div > div > div > div > span")

# Test sonuçları ve rapor görüntüleme locatorları
DEGERLENDIRME = (By.XPATH, "//a[contains(text(),'Değerlendirmeler')]")
VIEW_REPORT_LOCATOR = (By.XPATH, "//a[contains(text(),'Raporu Görüntüle')]")
FRONT_REPORT_ONE=(By.XPATH, "//button[contains(.,'Raporu Görüntüle')]")
FRONT_REPORT_TWO = (By.XPATH, "//div[2]/div[2]/button")
TOBETO_MODEL_LOCATOR = (By.XPATH, "//span[contains(.,'Tobeto İşte Başarı Modelim')]")

# Nitelik ve diğer alanlar için locatorlar
QUALIFICATION_LOCATOR = (By.XPATH, "(//button[@type='button'])[4]")
PERSONAL_INFO_LOCATOR = (By.XPATH, "//button[contains(.,'Başla')]")
EXPERIENCE_LOCATOR = (By.XPATH, "//span[contains(.,\'Deneyimlerim\')]")
LEARNING_VIEW_LOCATOR = (By.XPATH, "//span[contains(.,'Eğitim Hayatım')]")
SKILLS_VIEW_LOCATOR = (By.XPATH, "//span[contains(.,\'Yetkinliklerim\')]")
CERTIFICATES_VIEW_LOCATOR = (By.XPATH, "//span[contains(.,\'Sertifikalarım\')]")
SOCIAL_MEDIA_LOCATOR = (By.XPATH, "//span[contains(.,\'Medya Hesaplarım\')]")
LANGUAGES_VIEW_LOCATOR = (By.XPATH, "//span[contains(.,\'Yabancı Dillerim\')]")
SETTINGS_LOCATOR = (By.XPATH, "//span[contains(.,\'Ayarlar\')]")
