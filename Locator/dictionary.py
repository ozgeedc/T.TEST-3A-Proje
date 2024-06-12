from selenium.webdriver.common.by import By

Login_Data = "ozgecam@outlook.com"
Password_Data = "ozge-cam-5595"

username_Locator = (By.NAME, "email")
password_Locator = (By.NAME, "password")
iframe_locator = {
    "recaptcha_iframe": (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha']"),
    "recaptcha_checkbox": (By.CSS_SELECTOR, ".recaptcha-checkbox-border"),
}
Loginbutton_Locator =(By.XPATH, "//button[@type='submit']")

# Bu sözlük header > profil Alanı için sözlük içeriğidir.
ProfilB_Locator = (By.XPATH, "//a[contains(text(),'Profilim')]")
CV_popup_locator = (By.XPATH, "//button[@id='dropdown-basic']")
Onaybuton_locator = (By.CSS_SELECTOR, ".react-switch-bg")
Copybuton_locator = (By.CSS_SELECTOR, ".ms-3")
inbuton_locator = (By.CSS_SELECTOR, ".cv-linkedin")

# Bu alan Değerlendirmeler alanının sözlük kısmıdır.

degerlendirmelerButon_locator = (By.XPATH, "//a[contains(text(),'Değerlendirmeler')]")
RaporG_analiz_locator = (By.XPATH, "//a[contains(text(),'Raporu Görüntüle')]")
RaporG_front_locator = (By.XPATH, "//div[2]/div[2]/button")

# Bu alan Özniteliklerin görüntülenmesi alanıdır. 
nitelikone_locator = (By.XPATH,"(//button[@type='button'])[4]")

# Bu alan sayfanın alt kısmında bulunan Profil oluştur alanıdır.
creatprofil_locator = (By.XPATH, "//button[contains(.,'Başla')]")
deneyimlerim_locator = (By.XPATH,"//span[contains(.,\'Deneyimlerim\')]")
Ehayatım_locator = (By.XPATH,"//span[contains(.,'Eğitim Hayatım')]")
yetkinliklerim_locator = (By.XPATH,"//span[contains(.,\'Yetkinliklerim\')]")
sertifikalarim_locator = (By.XPATH,"//span[contains(.,\'Sertifikalarım\')]")
medyahesaplarim_locator = (By.XPATH,"//span[contains(.,\'Medya Hesaplarım\')]")
dillerim_locator = (By.XPATH,"//span[contains(.,\'Yabancı Dillerim\')]")
ayarlarim_locator = (By.XPATH,"//span[contains(.,\'Ayarlar\')]")