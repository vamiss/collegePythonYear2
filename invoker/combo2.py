from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.invokergame.com/")

action = ActionChains(driver)

driver.find_element(by="xpath", value="/html/body/form/div[3]/div[6]/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input").click()
driver.find_element(by="xpath", value="/html/body/form/div[3]/div[3]/div/table/tbody/tr/td[3]").click()

action.send_keys(Keys.ENTER)
action.perform()

while True:
    spellsData = driver.find_element(by="xpath", value="/html/body/form/div[3]/div[6]/div[2]/div[3]/div[1]/nobr/table/tbody/tr")
    spells = []
    for spell in spellsData.find_elements(by="tag name", value="span"):
        spells.append(spell.text)
    for _ in range(2):
        if "Cold Snap" in spells:
            action.send_keys("qqqrd")
        if "Ghost Walk" in spells:
            action.send_keys("qqwrd")
        if "Ice Wall" in spells:
            action.send_keys("qqerd")
        if "EMP" in spells:
            action.send_keys("wwwrd")
        if "Tornado" in spells:
            action.send_keys("wwqrd")
        if "Alacrity" in spells:
            action.send_keys("wwerd")
        if "Sun Strike" in spells:
            action.send_keys("eeerd")
        if "Forge Spirit" in spells:
            action.send_keys("eeqrd")
        if "Chaos Meteor" in spells:
            action.send_keys("eewrd")
        if "Deafening Blast" in spells:
            action.send_keys("qwerd")
        action.perform()
        sleep(0.1)