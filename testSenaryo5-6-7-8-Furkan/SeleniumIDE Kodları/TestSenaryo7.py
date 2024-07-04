{
  "id": "fd83604f-e277-44c4-9f9d-094fcc0f0535",
  "version": "2.0",
  "name": "TestSenaryo7",
  "url": " https://tobeto.com/giris",
  "tests": [{
    "id": "4a824a19-2293-48f2-954f-b0767333c2f6",
    "name": "TS7/TC1 Eğitimlerim Paneli’ne Yönlendirme",
    "commands": [{
      "id": "7200054e-8b76-4fef-b08c-827b98340d6e",
      "comment": "",
      "command": "open",
      "target": " https://tobeto.com/giris",
      "targets": [],
      "value": ""
    }, {
      "id": "03bad6a6-87ce-4f7b-8891-fd969e95d4bf",
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
      "id": "74fc286c-1c39-4cc3-9560-bd7fb4aed7c8",
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
      "id": "b7f6989c-7831-4420-af29-060583f250d4",
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
      "id": "1f8686d6-cbe3-4235-8c2f-9c770ab7d303",
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
      "id": "2de680f2-77f2-4ae6-a401-e52d5b5e9faf",
      "comment": "",
      "command": "click",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//button[@type='submit']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div[2]/div/div/div[4]/form/button", "xpath:idRelative"],
        ["xpath=//form/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "280c06f3-7cf1-4f96-8e46-898d45a13e4b",
      "comment": "",
      "command": "click",
      "target": "id=lessons-tab",
      "targets": [
        ["id=lessons-tab", "id"],
        ["css=#lessons-tab", "css:finder"],
        ["xpath=//button[@id='lessons-tab']", "xpath:attributes"],
        ["xpath=//ul[@id='myTab']/li[2]/button", "xpath:idRelative"],
        ["xpath=//li[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Eğitimlerim')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "25b586d0-777d-4d79-9fed-f2eb69f41be6",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=(//*[contains(@class, 'col-12')])[4]",
      "targets": [],
      "value": ""
    }, {
      "id": "919d1c2e-5021-461c-99cc-7f2e56a17e7c",
      "comment": "",
      "command": "click",
      "target": "css=.showMoreBtn:nth-child(2)",
      "targets": [
        ["css=.showMoreBtn:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='lessons-tab-pane']/div/div/div[2]", "xpath:idRelative"],
        ["xpath=//div/div[2]/div/div/div[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "916c5b56-eece-439d-a680-e2ffc6677d8e",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,0)",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "32a74207-450a-4ecd-a882-acd0e9e8071b",
    "name": "TS7/TC2 Kullanıcıya Atanan Eğitim İçeriklerinin Kontrolü ",
    "commands": [{
      "id": "1e42cbe8-3864-4a5d-a93e-b3291e760175",
      "comment": "",
      "command": "run",
      "target": "TS7/TC1 Eğitimlerim Paneli’ne Yönlendirme",
      "targets": [],
      "value": ""
    }, {
      "id": "36ca320b-1df0-458e-86e9-b660efa2fb09",
      "comment": "",
      "command": "click",
      "target": "css=#all-lessons-tab-pane .col-md-3:nth-child(1) .apply-btn",
      "targets": [
        ["css=#all-lessons-tab-pane .col-md-3:nth-child(1) .apply-btn", "css:finder"],
        ["xpath=//div[@id='all-lessons-tab-pane']/div/div/div/div[2]/button", "xpath:idRelative"],
        ["xpath=//div/div/div/div/div[2]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Eğitime Git')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "7d6c345d-638f-4599-adcb-cfb27fd9cd10",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["4a824a19-2293-48f2-954f-b0767333c2f6", "32a74207-450a-4ecd-a882-acd0e9e8071b"]
  }],
  "urls": ["https://tobeto.com/giris"],
  "plugins": []
}