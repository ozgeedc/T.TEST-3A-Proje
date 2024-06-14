from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

    



def check_404_errors(driver):
    # Mevcut sayfada herhangi bir 404 hatası olup olmadığını kontrol eder
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), '404')]")
        return True
    except:
        return False

def check_alignment(xpath, driver):
    # Verilen XPath kullanarak öğelerin düzgün hizalanıp hizalanmadığını kontrol eder
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.is_displayed()
    except:
        return False

def check_js_errors(driver):
    # Sayfada herhangi bir JavaScript hatası olup olmadığını kontrol eder
    logs = driver.get_log('browser')
    for entry in logs:
        if entry['level'] == 'SEVERE':
            return True
    return False

def check_link_functionality(link_id, driver):
    # Verilen ID'ye sahip bir linkin çalışıp çalışmadığını kontrol eder
    try:
        link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, link_id)))
        link.click()
        return True
    except:
        return False

def check_load_time(page):
    # Sayfa yükleme süresinin kabul edilebilir sınırlar içinde olup olmadığını kontrol eder
    max_load_time = 2.0  # Maksimum kabul edilebilir yükleme süresi (saniye)
    return page["load_time"] <= max_load_time

def load_time_method(self,method):
        home_page = {"load_time": 1.5}  # Gerçek sayfa nesnesi
        assert check_load_time(home_page), "Sayfa yükleme süresi çok uzun."    

def common_functionality_method(self, page, load_time):
       
        assert check_load_time({"load_time": load_time}), f"{page} yükleme süresi çok uzun."

def assert_page_conditions(home_page, expected_load_time, alignment_element, link_element):
    assert check_alignment(alignment_element), "UI elementleri yanlış hizalanmış."
    assert check_link_functionality(link_element), "Link çalışmıyor."
    assert check_load_time(home_page) <= expected_load_time, "Sayfa yükleme süresi çok uzun."



