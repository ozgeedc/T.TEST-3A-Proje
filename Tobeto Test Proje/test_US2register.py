import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from time import sleep
from constants import globalConstants as c

#Test Senaryosu 2 : Kayıt Ol Paneli Kontrolü 

class Test_Register:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def click_with_js(self, by, value):
        element = self.driver.find_element(by, value)
        self.driver.execute_script("arguments[0].click();", element)

    def register(self, email, password, passwordAgain, phone):
        self.driver.get(c.LOGIN_URL)
        
        # Click the signup button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".signup"))).click()

        firstName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))
        firstName.send_keys("pair2")

        lastName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "lastName")))
        lastName.send_keys("tobeto")

        emailInput = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
        emailInput.send_keys(email)

        password1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password1.send_keys(password)

        againPassword = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "passwordAgain")))
        againPassword.send_keys(passwordAgain)

        # Attempt to click the register button with retries
        for _ in range(3):
            try:
                registerbutton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mt-4")))
                registerbutton.click()
                break
            except ElementClickInterceptedException:
                print("Retrying to click the register button")
                sleep(1)
                continue

        sleep(2)

        AcikRizaMetni = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "contact")))
        AcikRizaMetni.click()

        uyeliksoz = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "membershipContrat")))
        uyeliksoz.click()

        emailonay = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "emailConfirmation")))
        emailonay.click()

        Aramaonay = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "phoneConfirmation")))
        Aramaonay.click()
        sleep(3)

        phoneNumber = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "phoneNumber")))
        phoneNumber.send_keys(phone)

        sleep(3)

        try:
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, c.R_IFRAME_CSS)))
            self.driver.switch_to.frame(iframe)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, c.R_CAPTCHA_CSS))).click()
            self.driver.switch_to.default_content()
        except TimeoutException:
            print("reCAPTCHA iframe not found")

        # Complete registration with retries
        for _ in range(3):  # Retry up to 3 times
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-yes"))).click()
                break
            except (ElementClickInterceptedException, TimeoutException):
                print("Retrying to click the .btn-yes button")
                sleep(1)
    
    #Case 1 : Başarılı Kayıt Ol Kontrolü

    def test_successful_register(self):
        self.register("pair23456789@gmail.com", "pair2tobeto2", "pair2tobeto2", "5376398437")
        sleep(2)
        try:
            success_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c.SUCCESS_CSS))).text
            assert "Tobeto Platform'a kaydınız başarıyla gerçekleşti." in success_message
            assert "Giriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin." in success_message
        except TimeoutException:
            print("Success message not found. Check if the registration was actually successful.")


    #Case 2: Kayıt ol sırasında istenen telefon numarası  karakter kontrolü 

    def test_invalid_phone1(self):
        self.register("pair2@gmail.com","pair2tobeto2","pair2tobeto2","54645")
        try:
            error_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, c.R1_ERROR_XPATH))).text
            assert "En az 10 karakter girmelisiniz." in error_message
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")


    def test_invalid_phone2(self):
        self.register("pair2tobeto@gmail.com","pair2tobeto2","pair2tobeto2","0000000000000")
        try:
            error_message2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c.R2_ERROR_CSS))).text
            assert "En fazla 10 karakter girebilirsiniz." in error_message2
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")
    
    #Case 3 : Geçersiz E-posta kontrolü 

   
    def test_invalid_email_register(self):
        self.register("e","pair2tobeto2", "pair2tobeto2", "5464522633")

        try:
            invalidErrorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.R3_ERROR_XPATH)))
            assert "Geçersiz e-posta adresi*" in invalidErrorMessage.text
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")
       

    # Case 4: Girdiğiniz e posta adresi ile kayıtlı üyelik bulunmaktadır uyarısının alınması.

    def test_unsuccessful_register(self):
        self.register("pair2tobeto2@gmail.com", "pair2tobeto2", "pair2tobeto2", "5464522633")
        sleep(2)
        try:
            registerErrorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c.R4_ERROR_CSS))).text
            assert "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır." in registerErrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")

    
    #Case 5: Şifrenin karakter sayı kontrolü.

    def test_password_less_than6(self):
        self.register("pair23@gmail.com", "123", "123", "5068372511")
        try:
            registerErrorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, c.R5_ERROR_XPATH))).text
            assert "• Şifreniz en az 6 karakterden oluşmalıdır." in registerErrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")

    #Case 6 : Şifre eşleşmeme kontrolü

    def test_password_match(self):
        self.register("pair234@gmail.com","1234567","7654321","5349652585")    
        try:
            passworderrorMessage = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, c.R6_ERROR_XPATH)))
            assert "• Şifreler eşleşmedi" in passworderrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")

    #Case 7 : Girilen bilgilerde 2 farklı hatalı kısım olduğunda

    def test_two_error(self):
        self.register("pair2tobeto2@gmail.com","123","123","5362698796")    
        try:
            twoErrorMessage = WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.XPATH, c.R7_ERROR_XPATH)))
            assert "• 2 errors occurred" in twoErrorMessage
        except TimeoutException:
            print("Error message not found. Check if the error occurred.")
