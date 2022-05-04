from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
import urllib
import wget
import os

#firefox = webbrowser.Mozilla(r"C:\Program Files\Mozilla Firefox\firefox.exe")
#firefox.open("https://web.whatsapp.com/")
#time.sleep(3)



os.remove('Enviar')

time.sleep(5)
wget.download('https://inicio.ahbb.org.br/Enviar')

time.sleep(5)
cobranca = open('Enviar')


myprofile = webdriver.FirefoxProfile(r'C:\Users\Lucas - TI\AppData\Roaming\Mozilla\Firefox\Profiles\0bicojn7.default-release')
navegador = webdriver.Firefox(firefox_profile=myprofile)


navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(3)
    



for contato in cobranca:
    pessoa,numero,mensagem = contato.split(';')
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)


    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
navegador.close()
