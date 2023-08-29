import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.youtube.com')

navegador.find_element('xpath', '//*[@id="container"]').click()    #ou .click se quiser clicar

#no symbol