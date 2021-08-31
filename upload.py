from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "SIGN IN"))
    )
    element.click()
except:
    driver.quit()





try:
    nextElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-vQzf8d"))
    )
    nextElement.click()
except:
    driver.quit()


try:
    passElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type=password]"))
    )
    passElement.send_keys("Meher@123")
except:
    driver.quit()
