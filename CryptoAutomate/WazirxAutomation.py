from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time


class SetUpWazirx():

    def launchWazirx(self):
        driver = webdriver.Chrome(executable_path="E:\CryptoProject\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://wazirx.com/")
        driver.implicitly_wait(20)
        credFile = open("E:\CryptoProject\Resources\credential.json", "r")
        cred = json.load(credFile)
        username = cred["username"]
        password = cred["password"]
        credFile.close()
        driver.find_element_by_xpath("//span[text()='Log in']").click()
        driver.find_element_by_xpath("//input[@type='email']").send_keys(username)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//span[text()='Login']").click()
        res = driver.find_element_by_xpath("(//a[@role='button'])[1]").is_displayed()
        while not res:
            time.sleep(5)
            res = driver.find_element_by_xpath("(//a[@role='button'])[1]").is_displayed()