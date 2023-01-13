from selene import browser, by, be, have
from selene.api import s, ss
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import sympy
import re
from latex2sympy2 import latex2sympy
from time import sleep
import tidydrfrost.robust_utils as robust
import tidydrfrost.js_utils as js

def start_task(url, n):
  robust.get_with_retry(url, ".skill")
  
  js.click(ss(".skill")[n].element("input"))
  
  js.click(s("#explorer-selection-practise"))
  start = s("#but-1-0")
  start.should(be.visible)
  Select(s("#task-numquestions").get_actual_webelement()).select_by_value('35')
  js.click(start)

def answer_question(answer, question_number = 1, answer_input = None, mq = False):
  if answer_input == None:
    if mq:
      answer_input = s(".answer-content").element(".eqnsolutions-answerinput")
    else:
      answer_input = s(".answer-content").element("input")
  
  if mq:
    js.mq_set(answer_input, str(answer))
  else:
    js.input_set(answer_input, str(answer))
  js.click(s("input[type='submit']"))
  final_checks(question_number)

def multiple_answers(answers, question_number = 1, mq = False):
  if mq:
    answer_boxes = s(".answer-content").elements(".eqnsolutions-answerinput")
  else:
    answer_boxes = s(".answer-content").elements("input")
  for ida, a in enumerate(answer_boxes[0:-1]):
    if mq:
      js.mq_set(a, str(answers[ida]))
    else:
      js.input_set(a, str(answers[ida]))
  answer_question(answers[-1], question_number, answer_input = answer_boxes[-1])

def try_two_answers(answers, question_number = 1, answer_input = None, mq = False):
  if answer_input == None:
    if mq:
      answer_input = s(".answer-content").element(".eqnsolutions-answerinput")
    else:
      answer_input = s(".answer-content").element("input")
  
  a1 = answers[0]
  a2 = answers[1]
  
  if mq:
    js.mq_set(answer_input, str(a1))
  else:
    js.input_set(answer_input, str(a1))
  js.click(s("input[type='submit']"))
  time_end = time.time() + 10
  while time.time() < time_end:
    if answer_is_incorrect():
      js.click(s(".close-modal"))
      break
    if detect_response(question_number == 34):
      final_checks(question_number)
      return True
    sleep(0.1)
  else:
    raise TimeoutError("Could not determine question response.")
  robust.close_modals()
  if mq:
    js.mq_set(answer_input, str(a2))
  else:
    js.input_set(answer_input, str(a2))
  js.click(s("input[type='submit']"))
  final_checks(question_number)

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

def final_checks(question_number):
  if question_number != 34:
    robust.close_modals()
    question_id = s(".question-form").get_attribute("id")
    try:
      js.click(s("#nextquestion-button"))
      s(".question-form").should_not(have.attribute("id", question_id))
      s(".question-content").element("p").should(be.visible)
      s(".question-form").element("input[type='submit']").should(be.visible)
    except:
      # Can not work the first time
      robust.close_modals()
      js.click(s("#nextquestion-button"))
      s(".question-form").should_not(have.attribute("id", question_id))
      s(".question-content").element("p").should(be.visible)
      s(".question-form").element("input[type='submit']").should(be.visible)
  else:
    s(".taskcomplete").should(be.visible)

def get_fraction(elem):
  n1 = elem.elements("mn")[0].text
  n2 = elem.elements("mn")[1].text
  fraction = n1 + "/" + n2
  return sympy.core.sympify(fraction, rational = True)

def submit(questions_answered):
  js.click(s("input[type='submit']"))
  final_checks(questions_answered)

def parse_mathjax(elem, simplify = True, exp_possible = False):
  elem.should(be.in_dom)
  math = js.execute_js("parse_mathjax", elem.get_actual_webelement(), exp = exp_possible)
  if simplify:
    return latex2sympy(math)
  else:
    return math

def parse_mixed_numbers(elem, simplify = True, exp_possible = False):
  elem.should(be.in_dom)
  math = js.execute_js("parse_mathjax", elem.get_actual_webelement(), exp = exp_possible)
  math = re.sub("([0-9]+)(\\\\frac{.+?}{.+?})", "(\\1+\\2)", math)
  if simplify:
    return latex2sympy(math)
  else:
    return math


