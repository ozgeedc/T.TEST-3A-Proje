import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

    




def check_load_time(page):
    # Sayfa yükleme süresinin kabul edilebilir sınırlar içinde olup olmadığını kontrol eder
    max_load_time = 2.0  # Maksimum kabul edilebilir yükleme süresi (saniye)
    return page["load_time"] <= max_load_time

def load_time_method(self,method):
        home_page = {"load_time": 1.5}  # Gerçek sayfa nesnesi
        assert check_load_time(home_page), "Sayfa yükleme süresi çok uzun."    

def common_functionality_method(self, page, load_time):
       
        assert check_load_time({"load_time": load_time}), f"{page} yükleme süresi çok uzun."

def assert_page_conditions(home_page, expected_load_time,check_load_time):
        assert check_load_time(home_page), "Sayfa yükleme süresi çok uzun."  

        assert check_load_time(home_page) <= expected_load_time, "Sayfa yükleme süresi çok uzun."    
            





