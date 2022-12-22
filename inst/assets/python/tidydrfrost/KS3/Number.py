from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re
from tidydrfrost.utils import answer_question

def addition_subtraction(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[0]\
    .find_element(By.TAG_NAME, "input")
  elem.click()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()
  
  cum_errors = 0
  
  while cum_errors < 5:
    try:
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_elements(By.TAG_NAME, "p")[1]
      question = elem.text
      question = question.replace("−", "-")
      answer = eval(question)
      answer_question(driver, answer)
      cum_errors = 0
    except:
      pass
      cum_errors += 1

def multiplication(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[2]\
    .find_element(By.TAG_NAME, "input")
  ActionChains(driver).move_to_element(elem).click(elem).perform()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()
  
  for a in range(50):
    try:
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_elements(By.TAG_NAME, "p")[1]
      question = elem.text
      question = question.replace("×", "*")
      answer = eval(question)
      answer_question(driver, answer)
    except:
      pass

def pictoral_division(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[3]\
    .find_element(By.TAG_NAME, "input")
  ActionChains(driver).move_to_element(elem).click(elem).perform()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()
  
  for a in range(50):
    try:
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_element(By.TAG_NAME, "p")
      question = re.search("[0-9]+.[0-9]+", elem.text).group(0)
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_question(driver, answer)
    except:
      pass

def division(driver):
  driver.get("https://www.drfrostmaths.com/explorer.php?noid=175")
  elem = driver.find_elements(By.CLASS_NAME, "skill")[4]\
    .find_element(By.TAG_NAME, "input")
  ActionChains(driver).move_to_element(elem).click(elem).perform()
  driver.find_element(By.ID, "explorer-selection-practise").click()
  Select(driver.find_element(By.ID, "task-numquestions")).select_by_value('35')
  driver.find_element(By.ID, "but-1-0").click()
  
  for a in range(50):
      elem = driver.find_element(By.CLASS_NAME, "question-content")\
        .find_elements(By.TAG_NAME, "p")[1]
      question = elem.text
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_question(driver, answer)
  
