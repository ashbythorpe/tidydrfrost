from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from tidydrfrost.decorators import task
import tidydrfrost.js_utils as js

@task("explorer.php?noid=177", 0)
def place_value(questions_answered):
  s(".desmos, .maths-line, .ui-sortable").should(be.visible)
  if ss(".desmos").size() > 0:
    question = s(".question-content").element("p")
    number = re.search("[0-9.]+", question.text).group(0)
    if number == ".":
      number = js.execute_js("get_place_value_number")
      utils.answer_question(number, questions_answered)
    else:
      index = js.execute_js("find_place_value_index", number)
      buttons = s(".answer-content").elements("input[type='radio']")
      js.click(buttons[index])
      utils.submit(questions_answered)
  elif ss(".ui-sortable").size() > 0:
    elements = s(".ui-sortable").elements("div")
    numbers = list(map(lambda x: float(x.text), elements))
    rank = sorted(range(len(numbers)), key=numbers.__getitem__)
    js.execute_js("sort_by_rank", rank)
    utils.submit(questions_answered)
  else:
    question = s(".question-content").elements("p")[1].text
    numbers = list(map(float, re.findall("[0-9.]+", question)))
    buttons = s(".answer-content").elements("input[type='radio']")
    labels = s(".answer-content").elements("label")
    labels_text = list(map(lambda x: x.text, labels))
    if numbers[0] == numbers[1]:
      answer = ["="]
    elif numbers[0] > numbers[1]:
      answer = [">", "≠"]
    else:
      answer = ["<", "≠"]
    index = list(map(lambda x: x in answer, labels_text)).index(True)
    js.click(buttons[index])
    utils.submit(questions_answered)

@task("explorer.php?noid=177", 1)
def decimal_addition_subtraction(questions_answered):
  element = s(".question-content").elements("p")[1]
  question = element.text
  question = question.replace("−", "-")
  answer = round(eval(question), 8)
  utils.answer_question(answer, questions_answered)
