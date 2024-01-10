from selenium import webdriver
from selenium.webDriver.Firefox.options import Options
from selenium.webDriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location(r"C:\Program Files\Mozilla Firefox\firefox.exe")
driver = webdriver.Firefox
driver.get("https://www.aviasales.ru")

data = driver.find_element(by="xpath", value="/html/body/div[7]/div[2]/div/div/div/div[2]/form/div[1]/div/button[1]")
searchFrom = driver.find_element(by="id", value="avia_form_origin-input")
searchTo = driver.find_element(by="id", value="avia_form_destination-input")

searchTo.click()
sleep(1)
searchTo.send_keys(Keys.BACKSPACE)
sleep(1)
searchTo.send_keys("Сочи")