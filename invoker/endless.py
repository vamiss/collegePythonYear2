from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.invokergame.com/")

action = ActionChains(driver)

driver.find_element(by="xpath", value="/html/body/form/div[3]/div[6]/div[2]/div[2]/div/table/tbody/tr[7]/td[1]/input").click()
driver.find_element(by="xpath", value="/html/body/form/div[3]/div[3]/div/table/tbody/tr/td[3]").click()

action.send_keys(Keys.ENTER)
action.perform()

while True:
    spell = driver.find_element(by="xpath", value="/html/body/form/div[3]/div[6]/div[2]/div[3]/div[1]/nobr/table/tbody/tr/td/span")
    if spell.text == "Cold Snap":
        action.send_keys("qqqr")
    elif spell.text == "Ghost Walk":
        action.send_keys("qqwr")
    elif spell.text == "Ice Wall":
        action.send_keys("qqer")
    elif spell.text == "EMP":
        action.send_keys("wwwr")
    elif spell.text == "Tornado":
        action.send_keys("wwqr")
    elif spell.text == "Alacrity":
        action.send_keys("wwer")
    elif spell.text == "Sun Strike":
        action.send_keys("eeer")
    elif spell.text == "Forge Spirit":
        action.send_keys("eeqr")
    elif spell.text == "Chaos Meteor":
        action.send_keys("eewr")
    elif spell.text == "Deafening Blast":
        action.send_keys("qwer")
    action.perform()
    sleep(0.1)