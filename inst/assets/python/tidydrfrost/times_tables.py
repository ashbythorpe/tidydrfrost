from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def times_tables_iter(driver):
  driver.get("https://www.drfrostmaths.com/timestables-game.php")
  
  sleep(1)
  
  start_div = driver.find_element(By.ID, "question")
  start_button = start_div.find_element(By.TAG_NAME, "a")
  start_button.click()
  question_el = driver.find_element(By.ID, "question")
  answer_box = driver.find_element(By.ID, "calculator-display")
  
  cum_errors = 0
  
  while cum_errors < 4:
    try:
      question = question_el.text
      question = question.replace("×", "*")
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_box.send_keys(answer)
      cum_errors = 0
    except:
      cum_errors += 1

def times_tables_game(driver, n):
  driver.get("https://www.drfrostmaths.com/timestables-game.php?id=" + str(n))
  start_div = driver.find_element(By.ID, "question")
  start_button = start_div.find_element(By.TAG_NAME, "a")
  start_button.click()
  answer_box = driver.find_element(By.ID, "calculator-display")
  
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
