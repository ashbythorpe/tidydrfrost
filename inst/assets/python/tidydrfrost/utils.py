from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re

def answer_question(driver, answer):
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
  sleep(1)

def get_points(driver):
  points_text = driver.find_element(By.CLASS_NAME, "taskcomplete")\
  .find_elements(By.TAG_NAME, "p")[0]
  points = int(re.search("[0-9]+", points_text.text).group(0))
  return points
