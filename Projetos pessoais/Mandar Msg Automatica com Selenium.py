import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# hashtag programação
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.youtube.com')

navegador.find_element('xpath', '//*[@id="container"]').click()    #ou .click se quiser clicar

#no symbol
"""

chromedrive_path = "C:/Users/henri/Desktop/navegadores/chromedriver/chromedrive.exe"
webdriver = webdriver.Chrome(executable_path = chromedrive_path)
time.sleep(2)
webdriver.get('https://news.ycombinator.com/submit')
time.sleep(2)

usuario = webdriver.find_element(By.NAME, 'acct')
usuario.send_keys('henriqueNDS')
senha = webdriver.find_element(By.NAME, 'pw')
senha.send_keys('0312Henrique')

button_login = webdriver.find_element(By.CSS_SELECTOR, 'body > form:nth-child(4) > input[type=submit]:nth-child(4)')
button_login.click()
time.sleep(2)