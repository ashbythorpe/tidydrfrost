from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def create_driver():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  return driver

def end_session(driver):
  sleep(2)
  
  driver.quit()

def login(driver, eml, pwd):
  driver.get("https://www.drfrostmaths.com/login.php")
  
  email = driver.find_element(By.NAME, "login-email")
  email.clear()
  email.send_keys(eml)
  
  password = driver.find_element(By.NAME, "login-password")
  password.clear()
  password.send_keys(pwd)
  
  login = driver.find_element(By.ID, "login-submit-button")
  login.click()
