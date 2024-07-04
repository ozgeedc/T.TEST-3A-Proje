#Login - invalid login 
LOGIN_URL ="https://tobeto.com/giris"
IFRAME_LOGIN_CSS="iframe[src^='https://www.google.com/recaptcha']"
CAPTCHA_LOGIN_CSS=".recaptcha-checkbox-border"
LOGIN_BUTTON_XPATH = "//button[@type='submit']"


#Register 
R_IFRAME_CSS = "iframe[src^='https://www.google.com/recaptcha']"
R_CAPTCHA_CSS= ".recaptcha-checkbox-border"
SUCCESS_CSS= ".success-payment-text"
R1_ERROR_XPATH= "//p[contains(.,\'En az 10 karakter girmelisiniz.\')]"
R2_ERROR_CSS="p:nth-child(4)"
R3_ERROR_XPATH="//div[@id='__next']/div/main/div[2]/div/div/form/p"
R4_ERROR_CSS=".alert-modal"
R5_ERROR_XPATH="//body/div[5]"
R6_ERROR_XPATH="//body/div[5]"
R7_ERROR_XPATH="//body/div[5]"


#Password forget
PASSWORD_FORGET_URL= "https://tobeto.com/sifremi-unuttum"
SEND_BUTTON_XPATH="//div[@id=\'__next\']/div/main/section/div/div/div/button"
FORGET_ERROR_MESSAGE_XPATH="//div[@id=\'__next\']/div/main/div[2]/div/div[2]"

#Chatbot
CHATBOT_ICON_XPATH="//*[@id='exw-launcher-frame']" 
LAUNCHER_BUTTON_XPATH="/html/body/div/div/button"
MESSAGE_WINDOW_XPATH="//iframe[@class='exw-conversation-container-frame']"
MESSAGE_WINDOW_FRAME_CSS="#exw-conversation-frame-body > div > div > div > div.exw-header-and-loading > div > div.exw-header-buttons > svg.exw-end-session-button.header-button"
MINIMIZE_BUTTON_CSS="svg.exw-minimize-button"
MESSAGE_INPUT_XPATH="/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/input"
MESSAGE_SEND_BUTTON_XPATH="/html/body/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]"
END_BUTTON_XPATH="/html/body/div/div/div/div[1]/div/div[3]/div/button[1]"
TEXT_AREA_XPATH="/html/body/div/div/div/div[2]/div[2]/div/div/form/textarea"
TEXT_SEND_BUTTON_XPATH="/html/body/div/div/div/div[2]/div[2]/div/div/form/button"
TOBETO_MESSAGE_XPATH="/html/body/div/div/div/div[2]/div[5]/div[2]/div/div/div/div/p"
TOBETO_MESSAGE2_XPATH="/html/body/div/div/div/div[2]/div[2]/div/div/div/h3"
EMOJI_BUTTON_XPATH="/html/body/div/div/div/div[3]/form/div/a"
EMOJI_PICKER_XPATH="/html/body/div/div/div/div[3]/div[1]/div/emoji-picker"
FILE_ATTACH_XPATH="/html/body/div/div/div/div[3]/form/div/button"
FILE_ATTACH_BUTTON_XPATH="/html/body/div/div/div/div[3]/div[2]/div[2]/button"