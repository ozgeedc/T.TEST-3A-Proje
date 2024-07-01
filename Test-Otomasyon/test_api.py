
import requests
import json

class Test_api_post():
  def test_api_post(self):
    url = "http://localhost:60805/api/Auth/Register"
    headers ={"Content-Type":"application/json"} 
    data = {"user": {"email":"3ATESTozge.cam@outlook.com",
                     "password":"Passw0rd!"},
                     "fistName":"Ozge",
                     "lastName":"CAM",
                     "nationalIdentity":"41149488501",
                     "phoneNumber":"05356253635"}
    response = requests.post(url,data=json.dumps(data),headers=headers)
    assert response.status_code == 201 #HTML Locator karşılaştırması yapar
    print(response.text)  # API'nin döndürdüğü yanıtı yazdır
    assert response.status_code == 201

    response_data = response.json()  # JSON yanıtını işle
    actual_email = response_data.get('email')  # Örnek olarak email'i kontrol edelim
    expected_email = "3ATESTozge.cam@outlook.com"

    assert actual_email == expected_email, f"Expected email: {expected_email}, Actual email: {actual_email}"
    
#Kullanıcı , Login işlemi yapılır.
  def test_api_login(self):
        url = "http://localhost:60805/api/Auth/Login"  # API giriş URL'sini buraya ekleyin
        headers = {"Content-Type": "application/json"}
        data = {
            "email": "3ATESTozge.cam@outlook.com",
            "password": "Passw0rd!"
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)

        assert response.status_code == 200
        print(response.json())

        response = requests.post(url, data=json.dumps(data), headers=headers)

        assert response.status_code == 200
        response_data = response.json()  # JSON yanıtını işle
        actual_email = response_data.get('email')  # Örnek olarak email'i kontrol edelim
        expected_email = "3ATESTozge.cam@outlook.com"

        assert actual_email == expected_email, f"Expected email: {expected_email}, Actual email: {actual_email}"

  def test_kayiteposta_post(self):
    url = "http://localhost:60805/api/Auth/Register"
    headers ={"Content-Type":"application/json"} 
    data = {"user": {"email":"3ATESTozge.cam@outlook.com",
                     "password":"Passw0rd!"},
                     "fistName":"Ozge",
                     "lastName":"CAM",
                     "nationalIdentity":"41149488501",
                     "phoneNumber":"05356253635"}
    response = requests.post(url,data=json.dumps(data),headers=headers)
    assert response.status_code == 500 #HTML Locator karşılaştırması yapar
    print(response.text)  # API'nin döndürdüğü yanıtı yazdır    


   # Kullanıcı ad alanını boş geçer
  def api_post_ad(self):
    url = "http://localhost:60805/api/Auth/Register"
    headers ={"Content-Type":"application/json"} 
    data = {"user": {"email":"pair2@outlook.com",
                     "password":"Passw0rd!"},
                     "fistName":"",
                     "lastName":"CAM",
                     "nationalIdentity":"41149488501",
                     "phoneNumber":"05356253635"} 
    response = requests.post(url,data=json.dumps(data),headers=headers)
    assert response.status_code == 400 #Bad Request
    print(response.text)  # API'nin döndürdüğü yanıtı yazdır       

  def api_post_soyad(self):
    url = "http://localhost:60805/api/Auth/Register"
    headers ={"Content-Type":"application/json"} 
    data = {"user": {"email":"pair2@outlook.com",
                     "password":"Passw0rd!"},
                     "fistName":"",
                     "lastName":"CAM",
                     "nationalIdentity":"41149488501",
                     "phoneNumber":"05356253635"} 
    response = requests.post(url,data=json.dumps(data),headers=headers)
    assert response.status_code == 400 #Bad Request
    print(response.text)  # API'nin döndürdüğü yanıtı yazdır      



