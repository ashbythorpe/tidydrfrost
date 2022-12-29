from selene import browser, by, be, have
from selene.api import s, ss
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from time import sleep
import tidydrfrost.robust_utils as robust

def start_task(url, n):
  robust.get_with_retry(url, ".skill")
  
  ss(".skill")[n].element("input").click()
  
  s("#explorer-selection-practise").click()
  start = s("#but-1-0")
  start.should(be.visible)
  Select(s("#task-numquestions").get_actual_webelement()).select_by_value('35')
  start.click()

def get_text(elem):
  try:
    return elem.text
  except:
    return elem.text

def set_value(elem, value):
  try:
    elem.set(value)
  except:
    elem.set(value)

def answer_question(answer, last_question = False, answer_input = None):
  if answer_input == None:
    answer_input = s(".answer-content").element("input")
    
  answer_input.set(answer)
  s("input[type='submit']").click()
  final_checks(last_question)

def try_two_answers(answers, last_question = False, answer_input = None):
  if answer_input == None:
    answer_input = s(".answer-content").element("input")
  
  a1 = answers[0]
  a2 = answers[1]
  
  answer_input.set(a1)
  s("input[type='submit']").click()
  time_end = time.time() + 10
  while time.time() < time_end:
    if answer_is_incorrect():
      s(".close-modal").click()
      break
    if detect_response(last_question):
      final_checks(last_question)
      return True
    sleep(0.5)
  else:
    raise TimeoutError("Could not determine question response.")
  robust.close_modals()
  answer_input.set(a2)
  s("input[type='submit']").click()
  final_checks(last_question)

def answer_is_incorrect():
  incorrect_messages = [
    "You may, wink wink, wish to reconsider your answer. Wink...", 
    "*Cough* *Cough* Perhaps try another answer. *Cough*", 
    "Psstt. A little bird told me that you may want to consider another answer. Wink wink.", 
    "This is Agent Winksworth. Middle name... 'That-Answer-Is-Wrong-Consider-Another'. [Exits via helicopter]", 
    "You may want to review your answer. Winkety wink.", 
    "This is Sir Winkington of Winksdon. One would like to inform you that you may wish to reconsider your answer."
  ]
  if ss(".modal").size() > 0:
    cond = (s(".modal").elements("p").size() > 1 and 
              s(".modal").elements("p")[1].text in incorrect_messages)
    return cond

def detect_response(last_question):
  if last_question:
    return ss(".taskcomplete").size() > 0
  else:
    return s("#doquestion-response").is_displayed()

def final_checks(last_question):
  if not last_question:
    robust.close_modals()
    question_id = s(".question-form").get_attribute("id")
    s("#nextquestion-button").scroll_to().click()
    s(".question-form").should_not(have.attribute("id", question_id))
    s(".question-content").element("p").should(be.visible)
    s(".answer-content").element("input").should(be.visible)
  else:
    s(".taskcomplete").should(be.visible)

while True:
  if True:
    break
else:
  print("a")

def parse_mathjax(elems):
  question = ""
  for el in elems:
    tag_name = el.tag_name
    if tag_name == "mrow":
      question += parse_mathjax(el.elements(by.xpath("./*")))
    elif tag_name == "msup":
      components = el.elements(by.xpath("./*"))
      question += components[0].text + "**" + components[1].text
    else:
      text = el.text
      if text == "−":
        question += "-"
      elif text == "×":
        question += "*"
      elif text == "÷":
        question += "/"
      else:
        question += text
  return question
