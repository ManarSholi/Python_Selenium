from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://github.com")
time.sleep(2)

signin_link = browser.find_element(by=By.LINK_TEXT, value="Sign in")
signin_link.click()
time.sleep(2)

email_box = browser.find_element(by=By.ID, value="login_field")
email_box.send_keys("manar.ghassan.sholi@gmail.com")
password_box = browser.find_element(by=By.ID, value="password")
password_box.send_keys("hellomanar321000")
password_box.submit()
time.sleep(2)

assert "ManarSholi" in browser.page_source

browser.quit()
