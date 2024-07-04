{
  "id": "45d0c2b8-4177-4d9b-8023-c3d070efb531",
  "version": "2.0",
  "name": "TestSenaryo6",
  "url": "https://tobeto.com",
  "tests": [{
    "id": "143fc6c4-77f3-4a78-817c-fb3d363fa16b",
    "name": "TS6/TC1 Hoşgeldiniz Paneli’ne Yönlendirme",
    "commands": [{
      "id": "d7f27914-c589-449a-8ffb-8215776d50b1",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "e457d82c-96f6-4c6d-a83d-3249b523a4fc",
      "comment": "",
      "command": "setWindowSize",
      "target": "1936x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "b7b5e77b-2b6a-428f-ad62-a47925f4ef0e",
      "comment": "",
      "command": "click",
      "target": "linkText=Giriş Yap",
      "targets": [
        ["linkText=Giriş Yap", "linkText"],
        ["css=.text-light", "css:finder"],
        ["xpath=//a[contains(text(),'Giriş Yap')]", "xpath:link"],
        ["xpath=//div[@id='__next']/div/section/nav/div/div/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/giris')]", "xpath:href"],
        ["xpath=//div/div/a", "xpath:position"],
        ["xpath=//a[contains(.,'Giriş Yap')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "c4d8de0f-6365-46d0-b727-78e51ec432a8",
      "comment": "",
      "command": "mouseOver",
      "target": "linkText=Giriş Yap",
      "targets": [
        ["linkText=Giriş Yap", "linkText"],
        ["css=.text-light", "css:finder"],
        ["xpath=//a[contains(text(),'Giriş Yap')]", "xpath:link"],
        ["xpath=//div[@id='__next']/div/section/nav/div/div/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/giris')]", "xpath:href"],
        ["xpath=//div/div/a", "xpath:position"],
        ["xpath=//a[contains(.,'Giriş Yap')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "80e6f2d5-2ebc-4f58-9586-72f0129a07d0",
      "comment": "",
      "command": "mouseOut",
      "target": "linkText=Giriş Yap",
      "targets": [
        ["linkText=Giriş Yap", "linkText"],
        ["css=.text-light", "css:finder"],
        ["xpath=//a[contains(text(),'Giriş Yap')]", "xpath:link"],
        ["xpath=//div[@id='__next']/div/section/nav/div/div/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/giris')]", "xpath:href"],
        ["xpath=//div/div/a", "xpath:position"],
        ["xpath=//a[contains(.,'Giriş Yap')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "edebb18c-a6fc-4c71-9fca-2ff9a8e3d57c",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.icon-input-group:nth-child(1) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7e9a96e3-fc6c-4bfa-a20a-ba43e0995c9a",
      "comment": "",
      "command": "type",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.icon-input-group:nth-child(1) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "furkangmsky@gmail.com"
    }, {
      "id": "18cce771-d74f-474f-aae0-4a6b692eb32c",
      "comment": "",
      "command": "click",
      "target": "name=password",
      "targets": [
        ["name=password", "name"],
        ["css=.icon-input-group:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4be0fcdb-250f-4946-b8b9-3e9406a7bc47",
      "comment": "",
      "command": "type",
      "target": "name=password",
      "targets": [
        ["name=password", "name"],
        ["css=.icon-input-group:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input", "xpath:idRelative"],
        ["xpath=//div[2]/input", "xpath:position"]
      ],
      "value": "Furkan-1445"
    }, {
      "id": "2e85fa5b-dfeb-44b1-9e92-95416c3eca31",
      "comment": "",
      "command": "click",
      "target": "css=.mt-4",
      "targets": [
        ["css=.mt-4", "css:finder"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/button", "xpath:idRelative"],
        ["xpath=//form/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "27352741-a4c7-444b-a5d8-cfd268c7001e",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.pack-bg-3 > .btn",
      "targets": [
        ["css=.pack-bg-3 > .btn", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/section[3]/div/div/div[2]/div/button", "xpath:idRelative"],
        ["xpath=//section[3]/div/div/div[2]/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c7f17e8c-fe4b-45ef-a809-c1b4beaf4747",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.pack-bg-3 > .btn",
      "targets": [
        ["css=.pack-bg-3 > .btn", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/section[3]/div/div/div[2]/div/button", "xpath:idRelative"],
        ["xpath=//section[3]/div/div/div[2]/div/button", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "c1c370fc-f667-4fc1-a761-1d3a0a2dd232",
    "name": "TS6/TC2 Hoşgeldiniz Paneli’nin Kontrolü",
    "commands": [{
      "id": "607ef87d-1bfd-466d-8775-733c6ddfc13c",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/platform",
      "targets": [],
      "value": ""
    }, {
      "id": "d112dffc-846e-43e0-a527-b8201e6b29ad",
      "comment": "",
      "command": "click",
      "target": "id=apply-tab",
      "targets": [],
      "value": ""
    }, {
      "id": "5aaf19fa-eff7-43f2-857e-1dc025710e29",
      "comment": "",
      "command": "click",
      "target": "id=lessons-tab",
      "targets": [],
      "value": ""
    }, {
      "id": "8b3c9f93-6487-4a5e-b076-6ea7737fdca4",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"all-lessons-tab-pane\"]/div/div[1]/div/div[2]/div/span[1]",
      "targets": [],
      "value": "Dr. Ecmel Ayral'dan Hoşgeldin Mesajı"
    }, {
      "id": "3fa76839-e0e1-4529-96ea-975c18196adc",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"all-lessons-tab-pane\"]/div/div[2]/div/div[2]/div/span[1]",
      "targets": [],
      "value": "Eğitimlere Nasıl Katılırım?"
    }, {
      "id": "5d45d7ab-b0cc-45b5-8153-f0c83b259b69",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"all-lessons-tab-pane\"]/div/div[3]/div/div[2]/div/span[1]",
      "targets": [],
      "value": "Herkes İçin Kodlama - 5B"
    }, {
      "id": "152c0987-57b1-4947-ae31-6288893743e9",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"all-lessons-tab-pane\"]/div/div[4]/div/div[2]/div/span[1]",
      "targets": [],
      "value": "Hoşgeldin Buluşması - 5"
    }, {
      "id": "08876619-0f41-4196-ba7a-8a5f0084b641",
      "comment": "",
      "command": "click",
      "target": "id=notification-tab",
      "targets": [],
      "value": ""
    }, {
      "id": "03879f4f-fc9b-4a3a-bcd8-85f2ea9f277b",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"notification-tab-pane\"]/div",
      "targets": [],
      "value": "Güncel Duyuru ve Haberler"
    }, {
      "id": "64c7ae40-edd5-4dc2-8a0f-53b2415cfde8",
      "comment": "",
      "command": "click",
      "target": "xpath=//*[@id=\"notification-tab-pane\"]/div/div[4]",
      "targets": [],
      "value": ""
    }, {
      "id": "e4a93285-bae8-49e8-b5dc-2629788c53d4",
      "comment": "",
      "command": "click",
      "target": "xpath=//*[@id=\"__next\"]/div/nav/div[1]/a",
      "targets": [],
      "value": ""
    }, {
      "id": "85031f1b-8c57-4e3e-acb8-95a25aea9f2a",
      "comment": "",
      "command": "click",
      "target": "id=mySurvey-tab",
      "targets": [],
      "value": ""
    }, {
      "id": "ed77ef7b-43ff-4529-8af9-b3b40a13c4fb",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"mySurvey-tab-pane\"]/div/div",
      "targets": [],
      "value": "Atanmış herhangi bir anketiniz bulunmamaktadır"
    }]
  }, {
    "id": "66b1f118-df9e-445d-a927-9a648b9e3d52",
    "name": "TS6/TC3 Sınavlarım Butonunun Kontrolü",
    "commands": [{
      "id": "b8ae69a5-89c0-46ea-bf6c-493c4ad3e040",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/platform",
      "targets": [],
      "value": ""
    }, {
      "id": "032bcfc5-6e07-4460-be3b-c81b7fee1aae",
      "comment": "",
      "command": "click",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[1]/section[3]/div/div/div[2]/div",
      "targets": [],
      "value": ""
    }, {
      "id": "0ad19937-7019-478d-99f8-1402a92489b5",
      "comment": "",
      "command": "click",
      "target": "xpath=//button[contains(text(), 'Raporu Görüntüle')]",
      "targets": [],
      "value": ""
    }, {
      "id": "f828e6ea-32a5-4e59-bc72-2a2694c8081e",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[contains(text(), 'Doğru')] ",
      "targets": [],
      "value": ""
    }, {
      "id": "46d037d4-954b-4fca-ae83-49854d21c6d0",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[contains(text(), 'Yanlış')]",
      "targets": [],
      "value": ""
    }, {
      "id": "f5e75ec6-6234-47a3-be4b-1b36e1305746",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[contains(text(), 'Boş')]",
      "targets": [],
      "value": ""
    }, {
      "id": "d81164aa-379d-4e12-920f-3573801f4ee2",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[contains(text(), 'Puan')]",
      "targets": [],
      "value": ""
    }, {
      "id": "e3414c46-4f70-4133-8fe9-efda1fece403",
      "comment": "",
      "command": "click",
      "target": "xpath=//button[contains(text(), 'Kapat')]",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "6c95f1d8-8951-458d-b1c9-9de03fbafe2f",
    "name": "TS6/TC4 Kişisel Alan Kontrolü",
    "commands": [{
      "id": "85fff61b-82fb-43c4-8f38-6696ea15780e",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/platform",
      "targets": [],
      "value": ""
    }, {
      "id": "47bbcc30-d97b-4e43-a31a-09fd23f00106",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0, document.body.scrollHeight)",
      "targets": [],
      "value": ""
    }, {
      "id": "ee839822-9263-4003-942e-013dd2cc5782",
      "comment": "",
      "command": "click",
      "target": "css=.pack-bg-2 > .btn",
      "targets": [
        ["css=.pack-bg-2 > .btn", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/section[4]/div/div/div/div/button", "xpath:idRelative"],
        ["xpath=//section[4]/div/div/div/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Başla')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "95f2cb78-c1f9-4a23-86b2-13bf91f1a76b",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/section/div/div/div[1]/div/a[1]",
      "targets": [],
      "value": ""
    }, {
      "id": "eab2d453-e76a-4a13-be26-909f3bee48a3",
      "comment": "",
      "command": "click",
      "target": "xpath=//*[@id=\"__next\"]/div/nav/div[1]/a",
      "targets": [],
      "value": ""
    }, {
      "id": "3f120f26-fcf8-4607-a852-bec34d5b9915",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0, document.body.scrollHeight)",
      "targets": [],
      "value": ""
    }, {
      "id": "42a11d6c-d772-4d45-a9a7-481a9d5d6c22",
      "comment": "",
      "command": "click",
      "target": "css=.pack-bg-3 > .btn",
      "targets": [
        ["css=.pack-bg-3 > .btn", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/section[4]/div/div/div[2]/div/button", "xpath:idRelative"],
        ["xpath=//section[4]/div/div/div[2]/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "40e0f77e-c3c0-4e82-86b5-aeaddc6d1196",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/section[2]/div/div/div[1]/div/span",
      "targets": [],
      "value": ""
    }, {
      "id": "b28a5c64-bef3-42ef-a239-fac54025dc57",
      "comment": "",
      "command": "click",
      "target": "css=.container-fluid > a > img",
      "targets": [
        ["css=.container-fluid > a > img", "css:finder"],
        ["xpath=//div[@id='__next']/div/nav/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "82a261fe-63bd-4e7e-96ce-7a86f725fd3f",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0, document.body.scrollHeight)",
      "targets": [],
      "value": ""
    }, {
      "id": "dd42a58e-4b7c-4d9d-a378-4197cd76aa02",
      "comment": "",
      "command": "click",
      "target": "css=.pack-bg-1 > .btn",
      "targets": [
        ["css=.pack-bg-1 > .btn", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/section[4]/div/div/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[3]/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "520869cb-7b63-454f-bb67-e21a3004d2f9",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"pills-education-tab\"]",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "5a9226f4-05ef-4135-a266-dc0e95a6b5a8",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": []
  }],
  "urls": ["https://tobeto.com/"],
  "plugins": []
}