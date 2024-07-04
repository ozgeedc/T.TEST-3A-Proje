{
  "id": "41dd5647-f59d-4767-9ab9-f35b90a86d0c",
  "version": "2.0",
  "name": "TestSenaryo5",
  "url": "https://tobeto.com",
  "tests": [{
    "id": "5ae6df51-18d5-49c2-8625-caf47ed36ff2",
    "name": "TS5/TC1 Filtresiz Tüm Eğitimlerin Takvim Üzerinde Gösterilmesi",
    "commands": [{
      "id": "23c955d3-8d20-4b84-8a57-435ad188268a",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/giris",
      "targets": [],
      "value": ""
    }, {
      "id": "8addb5d5-4236-4fc4-b85e-ba972cdec5a3",
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
      "id": "28b2f66e-d8f9-4dc6-ba56-9d00af9b0e60",
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
      "id": "e9996912-1321-4897-aedb-66871c936a1d",
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
      "id": "28cffca1-9ffc-49d5-8b15-0c104428dd60",
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
      "id": "a0547309-6bd3-49e6-adff-95bfd861f842",
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
      "id": "34e6b1ee-3728-477c-9397-87a27a3000ad",
      "comment": "",
      "command": "click",
      "target": "linkText=Takvim",
      "targets": [
        ["linkText=Takvim", "linkText"],
        ["css=.nav-item:nth-child(5) > .c-gray-3", "css:finder"],
        ["xpath=//a[contains(text(),'Takvim')]", "xpath:link"],
        ["xpath=//div[@id='__next']/div/nav/div/ul/li[5]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, '#')])[6]", "xpath:href"],
        ["xpath=//li[5]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Takvim')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "23451c79-e83b-4a8e-a628-9c1d649166c7",
      "comment": "",
      "command": "click",
      "target": "name=eventEnded",
      "targets": [
        ["name=eventEnded", "name"],
        ["css=.checkEventEnded", "css:finder"],
        ["xpath=//input[@name='eventEnded']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div[3]/div[2]/span/input", "xpath:idRelative"],
        ["xpath=//span/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "70013494-a441-4406-9be8-d9751b7cf224",
      "comment": "",
      "command": "click",
      "target": "name=eventContinue",
      "targets": [
        ["name=eventContinue", "name"],
        ["css=.checkEventContinue", "css:finder"],
        ["xpath=//input[@name='eventContinue']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div[3]/div[2]/span[2]/input", "xpath:idRelative"],
        ["xpath=//span[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4940d259-19f1-4c91-9d8e-96885cdba4da",
      "comment": "",
      "command": "click",
      "target": "name=eventBuyed",
      "targets": [
        ["name=eventBuyed", "name"],
        ["css=.checkEventBuyed", "css:finder"],
        ["xpath=//input[@name='eventBuyed']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div[3]/div[2]/span[3]/input", "xpath:idRelative"],
        ["xpath=//span[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4503aa16-df21-4bae-a2bc-ba2390f6cbec",
      "comment": "",
      "command": "click",
      "target": "name=eventNotStarted",
      "targets": [
        ["name=eventNotStarted", "name"],
        ["css=.checkEventNotStarted", "css:finder"],
        ["xpath=//input[@name='eventNotStarted']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div[3]/div[2]/span[4]/input", "xpath:idRelative"],
        ["xpath=//span[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "09cec3cb-710a-4b48-8b89-4554eeee4a4b",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-event-harness')]",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "f44a1467-8106-46a6-a68d-d05599b316a2",
    "name": "TS5/TC2 Eğitim Arama Filtresinin Kontrolü ",
    "commands": [{
      "id": "bd8683ab-0d30-445c-968c-3c073e03df09",
      "comment": "",
      "command": "run",
      "target": "TS5/TC1 Filtresiz Tüm Eğitimlerin Takvim Üzerinde Gösterilmesi",
      "targets": [],
      "value": ""
    }, {
      "id": "c4086316-8773-4565-ae15-e191e6a6273c",
      "comment": "",
      "command": "click",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7390d72b-2b42-4057-a9f2-bde257a29dac",
      "comment": "",
      "command": "type",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "Test"
    }, {
      "id": "f13b86a4-4b75-46c5-903d-7ecee583bf50",
      "comment": "",
      "command": "sendKeys",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "654f4569-34aa-4721-907f-5aa81364f539",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-event-harness')]",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "ce1dd215-67f6-4dff-a0a9-9e1ebdd3dbd7",
    "name": "TC5/TC3 Eğitmen Arama Filtresinin Kontrolü ",
    "commands": [{
      "id": "9508720c-a0cf-4c2f-8508-1f7be88dab67",
      "comment": "",
      "command": "run",
      "target": "TS5/TC1 Filtresiz Tüm Eğitimlerin Takvim Üzerinde Gösterilmesi",
      "targets": [],
      "value": ""
    }, {
      "id": "9fa4a612-7a37-4c8e-97b7-eb60670a9442",
      "comment": "",
      "command": "click",
      "target": "css=.css-8mmkcg",
      "targets": [
        ["css=.css-8mmkcg", "css:finder"]
      ],
      "value": ""
    }, {
      "id": "b461defa-8c66-4c18-9af6-19fe3ae2ebab",
      "comment": "",
      "command": "click",
      "target": "id=react-select-2-option-14",
      "targets": [
        ["id=react-select-2-option-14", "id"],
        ["css=#react-select-2-option-14", "css:finder"],
        ["xpath=//div[@id='react-select-2-option-14']", "xpath:attributes"],
        ["xpath=//div[@id='react-select-2-listbox']/div[15]", "xpath:idRelative"],
        ["xpath=//div[15]", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "5aa170e5-ca71-44bf-aca4-214efdf03b6e",
    "name": "TC5/TC4 Eğitmen ve Eğitim Arama Filtrelerinin Birlikte Kontrolü",
    "commands": [{
      "id": "67278738-f0d2-45e6-a011-7f5db6b4f6ef",
      "comment": "",
      "command": "run",
      "target": "TS5/TC1 Filtresiz Tüm Eğitimlerin Takvim Üzerinde Gösterilmesi",
      "targets": [],
      "value": ""
    }, {
      "id": "eacb55c8-f010-46f0-9bd6-71b67a851bb4",
      "comment": "",
      "command": "click",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "009392dd-a0f1-4817-bc19-3b606e4a7c51",
      "comment": "",
      "command": "click",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "125e0c25-7bcc-4ccc-9fe9-bae2f5d244a9",
      "comment": "",
      "command": "type",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "analist"
    }, {
      "id": "4cbb094b-de4c-4a69-bf9f-a72efd361bc8",
      "comment": "",
      "command": "sendKeys",
      "target": "id=search-event",
      "targets": [
        ["id=search-event", "id"],
        ["css=#search-event", "css:finder"],
        ["xpath=//input[@id='search-event']", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "0dd2d301-92ec-493a-bf62-8793de5aa57a",
      "comment": "",
      "command": "click",
      "target": "css=.css-8mmkcg > path",
      "targets": [
        ["css=.css-8mmkcg > path", "css:finder"]
      ],
      "value": ""
    }, {
      "id": "e46ccb6a-57d6-43b8-9060-919c2668cf79",
      "comment": "",
      "command": "click",
      "target": "id=react-select-2-option-16",
      "targets": [
        ["id=react-select-2-option-16", "id"],
        ["css=#react-select-2-option-16", "css:finder"],
        ["xpath=//div[@id='react-select-2-option-16']", "xpath:attributes"],
        ["xpath=//div[@id='react-select-2-listbox']/div[17]", "xpath:idRelative"],
        ["xpath=//div[17]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4ab44470-8f32-45ac-a374-0d29adf96cb9",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-event-harness')]",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "b4294859-2f70-45ed-a849-1826eab6ebdd",
    "name": "TC5/TC5 Tarih Yönlendirme Butonlarının Kontrolü ",
    "commands": [{
      "id": "1b793937-2c92-4c58-af86-691dd978b577",
      "comment": "",
      "command": "open",
      "target": "https://tobeto.com/giris",
      "targets": [],
      "value": ""
    }, {
      "id": "50ecb7ce-0cf1-4647-9eff-34653ee53c16",
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
      "id": "e402e6f0-0cd3-4ee8-8f4a-e1255034a02c",
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
      "id": "f9c87fc8-da15-4979-905c-dddc7addb875",
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
      "id": "7f0942c5-1d5e-4df8-a433-20d57175282d",
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
      "id": "287d74e5-9cde-491c-be1d-4e1d97b7175b",
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
      "id": "6bb04efc-cfcc-4988-9ffc-13bb3f0a2e42",
      "comment": "",
      "command": "click",
      "target": "linkText=Takvim",
      "targets": [
        ["linkText=Takvim", "linkText"],
        ["css=.nav-item:nth-child(5) > .c-gray-3", "css:finder"],
        ["xpath=//a[contains(text(),'Takvim')]", "xpath:link"],
        ["xpath=//div[@id='__next']/div/nav/div/ul/li[5]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, '#')])[6]", "xpath:href"],
        ["xpath=//li[5]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Takvim')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "1571c5dc-4178-40a4-bc33-c1c411085d5d",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-body fc-daygrid-body-unbalanced')]",
      "targets": [],
      "value": ""
    }, {
      "id": "2f6f1e78-6e09-4497-81f2-980dc32647ca",
      "comment": "",
      "command": "click",
      "target": "css=.fc-icon-chevron-left",
      "targets": [
        ["css=.fc-icon-chevron-left", "css:finder"],
        ["xpath=//div[@id='__next']/div/main/div/div/div[2]/div/div/div/div/div/div/button/span", "xpath:idRelative"],
        ["xpath=//div/div/div/div/div/button/span", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9ddc4df7-b37b-488c-869e-2d6f7b33cb67",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-body fc-daygrid-body-unbalanced')]",
      "targets": [],
      "value": ""
    }, {
      "id": "57e71227-d1ee-460e-856c-a05626c05dce",
      "comment": "",
      "command": "click",
      "target": "css=.fc-dayGridMonth-button",
      "targets": [
        ["css=.fc-dayGridMonth-button", "css:finder"],
        ["xpath=(//button[@type='button'])[7]", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div[2]/div/div/div/div/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[3]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Ay')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "16580106-ada1-468e-a9b9-ae7d35c2a077",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//div[contains(@class, 'fc-daygrid-body fc-daygrid-body-unbalanced')]",
      "targets": [],
      "value": ""
    }, {
      "id": "5832b7f9-d09c-496f-a49b-18afc9079d2d",
      "comment": "",
      "command": "click",
      "target": "css=.fc-timeGridWeek-button",
      "targets": [
        ["css=.fc-timeGridWeek-button", "css:finder"],
        ["xpath=(//button[@type='button'])[8]", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div[2]/div/div/div/div/div[3]/div/button[2]", "xpath:idRelative"],
        ["xpath=//div[3]/div/button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'Hafta')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "3e68cace-918b-410f-9068-d5681a371888",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[3]",
      "targets": [],
      "value": ""
    }, {
      "id": "f7e41b54-0329-4390-84cf-61d81ce2e878",
      "comment": "",
      "command": "click",
      "target": "css=.fc-timeGridDay-button",
      "targets": [
        ["css=.fc-timeGridDay-button", "css:finder"],
        ["xpath=(//button[@type='button'])[9]", "xpath:attributes"],
        ["xpath=//div[@id='__next']/div/main/div/div/div[2]/div/div/div/div/div[3]/div/button[3]", "xpath:idRelative"],
        ["xpath=//button[3]", "xpath:position"],
        ["xpath=//button[contains(.,'Gün')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "9197503b-79d9-42e5-9b92-fbec8ed297ed",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "xpath=//*[@id=\"__next\"]/div/main/div/div/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr[3]",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "ae19cff7-4b32-4ddf-9110-a41c229c0f03",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["5ae6df51-18d5-49c2-8625-caf47ed36ff2"]
  }],
  "urls": ["https://tobeto.com/"],
  "plugins": []
}