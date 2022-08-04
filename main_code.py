from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

text_to_transl = input("Введите строку для перевода: ")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get('https://translate.yandex.ru/?lang=en-ru&text=' + text_to_transl)

#driver.quit()