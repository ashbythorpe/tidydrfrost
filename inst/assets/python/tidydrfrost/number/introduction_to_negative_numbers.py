from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import sympy
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from tidydrfrost.decorators import task
import tidydrfrost.js_utils as js

@task("explorer.php?noid=195", 0)
def order_negative_numbers(questions_answered):
  s(".question-form").element("mi, .ui-sortable, .desmos").should(be.visible)
  if s(".question-content").elements("mi").size() > 0:
    el = s(".question-content").elements("p")[1].element("mjx-container")
    texts = re.findall("-?[0-9]+", utils.parse_mathjax(el, simplify = False))
    numbers = list(map(int, texts))
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
  elif s(".question-form").elements(".ui-sortable") > 0
    elements = s(".answer-content").elements(".ordered-row")
    numbers = list(map(lambda x: int(x.text), elements))  
    rank = sorted(range(len(numbers)), key=numbers.__getitem__)
    js.execute_js("sort_by_rank", rank)
    utils.submit(questions_answered)
  else:
    answer = js.execute_js("get_number_line_number")
    utils.answer_question(answer, questions_answered)
  
