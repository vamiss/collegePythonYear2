from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.invokergame.com/")

action = ActionChains(driver)

driver.find_element(by="xpath", value="/html/body/form/div[3]/div[6]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input").click()
driver.find_element(by="xpath", value="/html/body/form/div[3]/div[3]/div/table/tbody/tr/td[3]").click()

action.send_keys(Keys.ENTER)
action.perform()