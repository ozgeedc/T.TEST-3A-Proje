from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import locale
from datetime import datetime, timedelta
from time import sleep
from constants import globalConstants as c

#Test Senaryosu 4
class TestChatbot():
   def setup_method(self, method):
    chrome_options = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get(c.LOGIN_URL)
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()


#Case 1: Chatbot Simgesi ve Simgenin Açık veya Kapalı Kontrolü

   def test_chatbot_open_close(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
      launcherbutton = self.driver.find_element(By.XPATH, c.LAUNCHER_BUTTON_XPATH)
      launcherbutton.click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.MESSAGE_WINDOW_XPATH)))
      minimizebutton = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, c.MINIMIZE_BUTTON_CSS)))
      minimizebutton.click()
      try:
         self.driver.switch_to.default_content()
         WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
         launcherbutton.click()
         assert True
      except:
         assert False

#Case 2: Chatbot Mesaj Bölümü Kontrolü

   def test_chatbot_message(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
      self.driver.find_element(By.XPATH, c.LAUNCHER_BUTTON_XPATH).click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.MESSAGE_WINDOW_XPATH)))
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.MESSAGE_INPUT_XPATH)))
      self.driver.find_element(By.XPATH, c.MESSAGE_INPUT_XPATH).send_keys("Pair2 Tobeto", Keys.ENTER)
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.MESSAGE_SEND_BUTTON_XPATH)))
      self.driver.find_element(By.XPATH, c.MESSAGE_SEND_BUTTON_XPATH).click()
      sleep(10)
      assert self.driver.find_element(By.XPATH,c.TOBETO_MESSAGE_XPATH).text == "Tobeto’da ihtiyaçların ve kaynaklarına göre öğrenim yolculuğunu sen tasarlarsın. Tobeto değerlendirme araçlarıyla kendini test edebilirsin."


#Case 3: Chatbot Mesaj Bölümünü Sonlandırma 

   def test_chatbot_chat_end(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
      self.driver.find_element(By.XPATH, c.LAUNCHER_BUTTON_XPATH).click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.MESSAGE_WINDOW_XPATH)))
      WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, c.MESSAGE_WINDOW_FRAME_CSS)))
      self.driver.find_element(By.CSS_SELECTOR, c.MESSAGE_WINDOW_FRAME_CSS).click()
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.END_BUTTON_XPATH)))
      self.driver.find_element(By.XPATH, c.END_BUTTON_XPATH).click()

      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.TEXT_AREA_XPATH)))
      self.driver.find_element(By.XPATH, c.TEXT_AREA_XPATH).send_keys("Teşekkürler")
      sleep(1)
      self.driver.find_element(By.XPATH, c.TEXT_SEND_BUTTON_XPATH).click()
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.TOBETO_MESSAGE2_XPATH)))
      assert self.driver.find_element(By.XPATH, c.TOBETO_MESSAGE2_XPATH).text == "Geri bildiriminiz için teşekkürler!"

#Case 4: Emoji Kontrolü 
 
   def test_chatbot_emoji(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
      self.driver.find_element(By.XPATH, c.LAUNCHER_BUTTON_XPATH).click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.MESSAGE_WINDOW_XPATH)))
      EmojiButton = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.EMOJI_BUTTON_XPATH)))
      EmojiButton.click()
      shadow_host = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.EMOJI_PICKER_XPATH)))
      script = '''
        const shadowRoot = arguments[0].shadowRoot;
        const emoji = shadowRoot.querySelector('#skintone-button');
        emoji.click();'''
      self.driver.execute_script(script, shadow_host)
      assert True

   def test_chatbot_file(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.CHATBOT_ICON_XPATH)))
      self.driver.find_element(By.XPATH, c.LAUNCHER_BUTTON_XPATH).click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, c.MESSAGE_WINDOW_XPATH)))
      fileattach = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.FILE_ATTACH_XPATH)))
      fileattach.click()
      button = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, c.FILE_ATTACH_BUTTON_XPATH)))
      assert button.text == "Dosya Seçiniz"
