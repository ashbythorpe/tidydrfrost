from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
from time import sleep

def create_driver():
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  return driver

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

def times_tables_iter(driver):
  driver.get("https://www.drfrostmaths.com/timestables-game.php")
  
  start_div = driver.find_element(By.ID, "question")
  start_button = start_div.find_element(By.TAG_NAME, "a")
  start_button.click()
  answer_box = driver.find_element(By.ID, "calculator-display")
  
  n_answered = 0
  start = datetime.utcnow()
  
  # Stop if 30 seconds pass or if 30 questions are answered
  # Adjust this to get a higher score
  while (datetime.utcnow() - start < timedelta(seconds=30)) and n_answered < 30:
    try:
      question_el = driver.find_element(By.ID, "question")
      question = question_el.text
      question = question.replace("×", "*")
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_box.clear()
      answer_box.send_keys(answer)
      # Wait for 0.2 seconds between each question
      # Could probably be shorter
      sleep(0.2)
      n_answered += 1
    except:
      # Stop on error
      break
