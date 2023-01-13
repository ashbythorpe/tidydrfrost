from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from tidydrfrost.decorators import task
import tidydrfrost.js_utils as js

@task("explorer.php?noid=191", 0)
def continue_sequence(questions_answered):
  element = s(".question-content").elements("p")[0]
  numbers = re.findall("[-0-9]+", element.text)
  rel_numbers = list(map(lambda x: int(x), numbers[0:3]))
  last = int(numbers[-1])
  answer_boxes = s(".answer-content").elements("input")
  if rel_numbers[1] - rel_numbers[0] == rel_numbers[2] - rel_numbers[1]:
    diff = rel_numbers[1] - rel_numbers[0]
    answer = last + diff
    for el in answer_boxes[0:-1]:
      js.input_set(el, answer)
      answer += diff
  else:
    mult = rel_numbers[1]/rel_numbers[0]
    answer = last * mult
    for el in answer_boxes[0:-1]:
      js.input_set(el, answer)
      answer *= mult
  utils.answer_question(answer, questions_answered, answer_input = answer_boxes[-1])

@task("explorer.php?noid=191", 1)
def later_terms(questions_answered):
  elements = s(".question-content").elements("p")
  numbers = re.findall("[-0-9]+", elements[1].text)
  rel_numbers = list(map(lambda x: int(x), numbers[0:3]))
  n = int(re.search("[0-9]+", elements[2].text).group(0))
  if rel_numbers[1] - rel_numbers[0] == rel_numbers[2] - rel_numbers[1]:
    diff = rel_numbers[1] - rel_numbers[0]
    answer = rel_numbers[0] + diff * (n - 1)
  else:
    mult = rel_numbers[1]/rel_numbers[0]
    answer = rel_numbers[0] * mult ** (n - 1)
  utils.answer_question(answer, questions_answered)

