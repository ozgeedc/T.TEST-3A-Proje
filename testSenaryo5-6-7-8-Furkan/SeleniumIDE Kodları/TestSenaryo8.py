{
  "id": "6651cc66-94de-4878-9654-b9c5602a50a3",
  "version": "2.0",
  "name": "TestSenaryo8",
  "url": "https://tobeto.com",
  "tests": [{
    "id": "fc42ab4a-2c58-48fc-99bd-eb5f65a63df7",
    "name": "TS8/TC1 Duyuru ve Haberlerim Kısmına Erişim Kontrolü",
    "commands": [{
      "id": "fbf805cb-70f0-4ab9-bffd-6f526140d6a0",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/giris",
      "targets": [],
      "value": ""
    }, {
      "id": "365abf0a-5678-4c1a-a944-14885626a721",
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
      "id": "d958a1c3-64f2-44b5-84b6-1241999d4ca7",
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
      "id": "3111e002-1d6a-46b3-be30-a77cdf8aedba",
      "comment": "",
      "command": "click",
      "target": "css=.icon-input-group:nth-child(2)",
      "targets": [
        ["css=.icon-input-group:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]", "xpath:idRelative"],
        ["xpath=//form/div[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4ab91fa4-d171-426a-9309-4d10084e397b",
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
      "id": "3c508e45-6836-4294-9c7c-2956e9212aa3",
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
      "id": "b0a03dc2-18cf-4573-a999-129fe3eee6ea",
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
      "id": "4525c572-637f-4edf-9f0a-9726acdce5d4",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[1]/section[1]/div/div[2]/div/h3/span[3]",
      "targets": [],
      "value": "hoş geldin"
    }, {
      "id": "4811f8b5-a52b-4b90-90d8-bc39ddc28c1c",
      "comment": "",
      "command": "executeScript",
      "target": "window.scrollBy(0, 1000)",
      "targets": [],
      "value": ""
    }, {
      "id": "4af2e072-6da1-48d1-8682-b347f64f08d4",
      "comment": "",
      "command": "click",
      "target": "id=notification-tab",
      "targets": [
        ["id=notification-tab", "id"],
        ["css=#notification-tab", "css:finder"],
        ["xpath=//button[@id='notification-tab']", "xpath:attributes"],
        ["xpath=//ul[@id='myTab']/li[3]/button", "xpath:idRelative"],
        ["xpath=//li[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Duyuru ve Haberlerim')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "21f9153c-b537-4a55-9324-e8fe73fb6f81",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"notification-tab-pane\"]/div",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "37015185-8e78-45d4-b2e8-1858968e1da1",
    "name": "TS8/TC2 Duyuru ve Haberlerim Kısmı Filtreleme İşlemlerinin Kontrolü ",
    "commands": [{
      "id": "1571a744-739b-4234-bcdc-d60bb9304e4f",
      "comment": "",
      "command": "run",
      "target": "TS8/TC1 Duyuru ve Haberlerim Kısmına Erişim Kontrolü",
      "targets": [],
      "value": ""
    }, {
      "id": "13a7c45c-2c3a-4aa1-ab8e-49f7715077aa",
      "comment": "",
      "command": "click",
      "target": "css=.showMoreBtn:nth-child(4)",
      "targets": [
        ["css=.showMoreBtn:nth-child(4)", "css:finder"],
        ["xpath=//div[@id='notification-tab-pane']/div/div[4]", "xpath:idRelative"],
        ["xpath=//div[3]/div/div[3]/div/div[4]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ca42f3f2-42cf-41a0-8730-ca9743967346",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,0)",
      "targets": [],
      "value": ""
    }, {
      "id": "20d3fda7-2088-40a5-846c-9c2d129e61b3",
      "comment": "Kullanıcıya atanan ilk \"dokuz\" duyuru ve haber görüntülenebilmelidir",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[2]/div[2]",
      "targets": [],
      "value": ""
    }, {
      "id": "ee748106-da4f-43fe-8c21-4a4871a0ae96",
      "comment": "Duyuru ve Haberlerin üzerinde filtreleme işlemleri için gerekli arama motoru, tür, organizasyon, sıralama tercihlerinin yapılabileceği alanlar ve okunmuş olanları gizleyebilmek için bir buton bulunmalıdır",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[2]/div[1]",
      "targets": [],
      "value": ""
    }, {
      "id": "05406ef7-a6f5-45cd-a238-ac05244c77ac",
      "comment": "duyuru ve haberlerin altında bir \"pagination\" buton bulunmalı ve sonraki duyuru ve haberler arasında geçiş yapılabilmelidir. ",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[2]/div[2]/ul",
      "targets": [],
      "value": ""
    }, {
      "id": "520ddd19-460d-4c5a-9cbd-04b93e42c813",
      "comment": "",
      "command": "click",
      "target": "css=.page-item:nth-child(5) > .page-link",
      "targets": [
        ["css=.page-item:nth-child(5) > .page-link", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div[2]/ul/li[5]/a", "xpath:idRelative"],
        ["xpath=//div[2]/ul/li[5]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "cb4ae945-7792-4aa3-8d77-6c75eb3f02bd",
      "comment": "",
      "command": "click",
      "target": "css=.page-item:nth-child(5) > .page-link",
      "targets": [
        ["css=.page-item:nth-child(5) > .page-link", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div[2]/ul/li[5]/a", "xpath:idRelative"],
        ["xpath=//div[2]/ul/li[5]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d2ad1620-1342-46c9-8383-21cd5fb3fd41",
      "comment": "",
      "command": "click",
      "target": "id=search",
      "targets": [
        ["id=search", "id"],
        ["css=#search", "css:finder"],
        ["xpath=//input[@id='search']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a99f9b9b-7ae5-4e77-b367-b5bd66ff82bf",
      "comment": "",
      "command": "type",
      "target": "id=search",
      "targets": [
        ["id=search", "id"],
        ["css=#search", "css:finder"],
        ["xpath=//input[@id='search']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "Ocak Ayı"
    }, {
      "id": "e60d1383-f852-4a9b-8407-91050a06359c",
      "comment": "",
      "command": "sendKeys",
      "target": "id=search",
      "targets": [
        ["id=search", "id"],
        ["css=#search", "css:finder"],
        ["xpath=//input[@id='search']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "b7043225-1ec9-4231-b17a-cc138c2a0380",
      "comment": "",
      "command": "verifyText",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[2]/div[2]/div/p",
      "targets": [],
      "value": "Bir duyuru bulunmamaktadır."
    }, {
      "id": "0613b57c-6d28-4c96-9055-f10d351bae16",
      "comment": "",
      "command": "executeScript",
      "target": "window.location.reload()",
      "targets": [],
      "value": ""
    }, {
      "id": "3d6df0a8-47ab-4994-acf8-379e80436e88",
      "comment": "",
      "command": "click",
      "target": "css=.ms-0",
      "targets": [
        ["css=.ms-0", "css:finder"],
        ["xpath=(//button[@type='button'])[4]", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[2]/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Tür')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "301d5eb0-64e5-4e09-8c34-a37ba23d1f40",
      "comment": "",
      "command": "click",
      "target": "id=typeAnnouncement",
      "targets": [
        ["id=typeAnnouncement", "id"],
        ["css=#typeAnnouncement", "css:finder"],
        ["xpath=//input[@id='typeAnnouncement']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[2]/ul/li[2]/div/input", "xpath:idRelative"],
        ["xpath=//li[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2684bcef-faf3-453b-8dad-91dfd0489f79",
      "comment": "",
      "command": "click",
      "target": "css=.ms-0",
      "targets": [
        ["css=.ms-0", "css:finder"],
        ["xpath=(//button[@type='button'])[4]", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[2]/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Tür')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "2da580b6-6949-4dde-b72e-3ce350606af5",
      "comment": "Kullanıcının seçtiği tercih sonucunda ilgili bölüm filtrelenmeli ve sadece o alana ait veriler gelmelidir",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div[2]/div[2]",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "65da8306-4676-499a-a193-a1d660fb532e",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["fc42ab4a-2c58-48fc-99bd-eb5f65a63df7"]
  }],
  "urls": ["https://tobeto.com/"],
  "plugins": []
}