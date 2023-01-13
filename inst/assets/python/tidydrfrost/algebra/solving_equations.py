from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import math
import string
import sigfig
import sympy
from latex2sympy2 import latex2sympy
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from sympy.parsing.sympy_parser import parse_expr
from tidydrfrost.decorators import task

@task("explorer.php?noid=192", 0)
def simple_substitution(questions_answered):
  els = s(".question-content").element("p").elements("mjx-container")
  question = utils.parse_mathjax(els[0])
  value = utils.parse_mathjax(els[1], simplify = False)
  
  answer = question.subs(
    re.search(".+(?==)", value).group(0).replace(" ", ""),
    latex2sympy(re.search("(?<==).+", value).group(0))
  )
  utils.answer_question(answer, questions_answered)

@task("explorer.php?noid=192", 1)
def solve_one_step(questions_answered):
  math = s(".question-content").elements("p")[1].element("mjx-container")
  question = utils.parse_mathjax(math)
  if isinstance(question, list):
    answer = question[0].rhs
  else:
    answer = question
  utils.answer_question(str(answer), questions_answered, mq = True)
