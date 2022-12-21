from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
from time import sleep
import re

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
  while (datetime.utcnow() - start < timedelta(seconds=30)) and n_answered < 100:
    try:
      question_el = driver.find_element(By.ID, "question")
      question = question_el.text
      question = question.replace("×", "*")
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_box.clear()
      answer_box.send_keys(answer)
      n_answered += 1
    except:
      # Stop on error
      break

def times_tables_game(driver, n):
  driver.get("https://www.drfrostmaths.com/timestables-game.php?id=" + str(n))
  start_div = driver.find_element(By.ID, "question")
  start_button = start_div.find_element(By.TAG_NAME, "a")
  start_button.click()
  answer_box = driver.find_element(By.ID, "calculator-display")
  
  power_questions = [4, 28, 29]
  
  for a in range(40):
    try:
      if n == 4:
        # Powers
        question_el = driver.find_element(By.ID, "question")
        power_el = question_el.find_element(By.TAG_NAME, "sup")
        relevant_question = question_el.text[0:-1]
        question = relevant_question + " ** " + power_el.text
        answer = round(eval(question))
      elif n == 28:
        # Square numbers
        question_el = driver.find_element(By.ID, "question")
        x = eval(question_el.text[0:-1])
        answer = x * x
      elif n == 29:
        # Cube numbers
        question_el = driver.find_element(By.ID, "question")
        x = eval(question_el.text[0:-1])
        answer = x * x * x
      else:
        question_el = driver.find_element(By.ID, "question")
        question = question_el.text
        question = question.replace("×", "*")
        question = question.replace("÷", "/")
        answer = round(eval(question))
      answer_box.clear()
      answer_box.send_keys(answer)
    except:
      break

def addition_subtraction(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[0]\
    .find_element(By.TAG_NAME, "input")
  elem.click()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()

  for a in range(40):
    try:
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_elements(By.TAG_NAME, "p")[1]
      question = elem.text
      question = question.replace("−", "-")
      answer_question(driver, question)
    except:
      break

def multiplication(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[2]\
    .find_element(By.TAG_NAME, "input")
  ActionChains(driver).move_to_element(elem).click(elem).perform()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()
  
  for a in range(40):
    try:
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_elements(By.TAG_NAME, "p")[1]
      question = elem.text
      question = question.replace("×", "*")
      answer_question(driver, question)
    except:
      break

def answer_question(driver, question):
  answer = eval(question)
  answer_input = driver.find_element(By.CLASS_NAME, "answer-content")\
    .find_element(By.TAG_NAME, "input")
  answer_input.clear()
  answer_input.send_keys(answer)
  submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
  submit_button.click()
  sleep(1)
  try:
    # Close modals (e.g. trophies)
    driver.find_element(By.CLASS_NAME, "close-modal").click()
  except:
    pass
  next_question = driver.find_element(By.ID, "nextquestion-button")
  ActionChains(driver).move_to_element(next_question).click(next_question).perform()
  sleep(0.5)
