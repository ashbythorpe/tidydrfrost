from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import sympy
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from tidydrfrost.decorators import task
import tidydrfrost.js_utils as js

@task("explorer.php?noid=178", 0)
def shape_fractions(questions_answered):
  s(".question-content").element(".desmos").should(be.visible)
  fraction = js.execute_js("get_filled_fraction")
  answer = sympy.core.sympify(fraction, rational = True)
  utils.multiple_answers([answer.p, answer.q], questions_answered)

@task("explorer.php?noid=178", 1)
def equivalent_fractions(questions_answered):
  s(".question-form")\
    .element(by.xpath('(.//div[@class="question-content"]/p[position() = 2])|(.//div[contains(@class, "ui-sortable")])'))\
    .should(be.visible)
  if s(".question-form").elements(".ui-sortable").size() > 0:
    rows = s(".answer-content").elements("mfrac")
    f1 = utils.get_fraction(rows[0])
    f2 = utils.get_fraction(rows[1])
    if f1 >= f2:
      js.execute_js("swap_sortable_elems")
    utils.submit(questions_answered)
  elif s(".question-content").elements("mi").size() > 0:
    question = s(".question-content").elements("p")[1].element("math")
    first_fraction = question.element("mfrac")
    n1 = first_fraction.elements("mn")[0].text
    n2 = first_fraction.elements("mn")[1].text
    n3 = question.elements("mfrac")[1].element("mn").text
    answer = round(int(n3) / int(n2) * int(n1), 8)
    utils.answer_question(answer, questions_answered)
  elif s(".question-content").elements("mfrac").size() > 0:
    frac = s(".question-content").elements("p")[1].element("mfrac")
    n1 = frac.elements("mn")[0].text
    n2 = frac.elements("mn")[1].text
    fraction = n1 + "/" + n2
    answer = sympy.core.sympify(fraction, rational = True)
    utils.multiple_answers([answer.p, answer.q], questions_answered)
  else:
    question = s(".question-content").element("p").text
    numbers = re.findall("[0-9]+", question)
    if int(numbers[1]) >= int(numbers[0]):
      frac = numbers[0] + "/" + numbers[1]
    else:
      frac = numbers[1] + "/" + numbers[0]
    answer = sympy.core.sympify(frac, rational = True)
    utils.multiple_answers([answer.p, answer.q], questions_answered)

@task("explorer.php?noid=178", 2)
def fraction_integer_division(questions_answered):
  n1, n2, n3 = s(".question-content").elements("p")[1].elements("mn")
  final = n1.text + "/" + n2.text + "/" + n3.text
  answer = sympy.core.sympify(final, rational = True)
  utils.multiple_answers([answer.p, answer.q], questions_answered)

@task("explorer.php?noid=178", 3)
def order_fractions(questions_answered):
  if s(".question-content").elements("mi").size() > 0:
    els = s(".question-content").elements("p")[1].elements("mfrac")
    fractions = list(map(utils.get_fraction, els))
    buttons = s(".answer-content").elements("input[type='radio']")
    labels = s(".answer-content").elements("label")
    labels_text = list(map(lambda x: x.text, labels))
    if fractions[0] == fractions[1]:
      answer = ["="]
    elif fractions[0] > fractions[1]:
      answer = [">", "≠"]
    else:
      answer = ["<", "≠"]
    index = list(map(lambda x: x in answer, labels_text)).index(True)
    js.click(buttons[index])
    utils.submit(questions_answered)
  else:
    elements = s(".answer-content").elements("math")
    numbers = list(map(parse_number, elements))
    rank = sorted(range(len(numbers)), key=numbers.__getitem__)
    js.execute_js("sort_by_rank", rank)
    utils.submit(questions_answered)

@task("explorer.php?noid=178", 4)
def mixed_addition_subtraction(questions_answered):
  math = s(".question-content").element("mjx-container")
  question = utils.parse_mixed_numbers(math)
  answer = question.doit()
  answers = [answer.p // answer.q, answer.p % answer.q, answer.q]
  utils.multiple_answers(answers, questions_answered)

@task("explorer.php?noid=178", 5)
def fraction_amount(questions_answered):
  frac = s(".question-content").element("p").element("mfrac")
  fraction = utils.get_fraction(frac)
  number = int(s(".question-content").element("p").elements("math")[-1].text)
  answer = fraction * number
  utils.answer_question(float(answer), questions_answered)

@task("explorer.php?noid=178", 6)
def amount_before_fraction(questions_answered):
  if s(".question-content").elements("mi").size() > 0:
    question = s(".question-content").elements("p")[1]
    frac = question.element("mfrac")
    fraction = utils.get_fraction(frac)
    number = int(question.elements("mn")[-1].text)
  else:
    frac = s(".question-content").element("p").element("mfrac")
    fraction = utils.get_fraction(frac)
    number = int(re.findall("[0-9]+", s(".question-content").element("p").text)[1])
  answer = number / fraction
  utils.answer_question(float(answer), questions_answered)



# THIS IS NOT A TASK
def parse_number(elem):
  if elem.elements("mfrac").size() > 0:
    frac = elem.element("mfrac")
    els = frac.elements("mn")
    fraction = els[0].text + "/" + els[1].text
    return sympy.core.sympify(fraction, rational = True)
  else:
    text = elem.text
    if "%" in text:
      fraction = text.replace("%", "") + "/100"
      return sympy.core.sympify(fraction, rational = True)
    else:
      return float(text)

