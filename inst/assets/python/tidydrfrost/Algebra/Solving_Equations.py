from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import math
import string
import sigfig
import sympy
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import T

def simple_substitution():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=192", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      els = s(".question-content").element("p").elements("math")
      question = els[0].text.replace("−", "-").replace("×", "*").replace("÷", "/")
      if els[0].elements("msup").size() == 0 and els[0].elements("mfrac").size() == 0:
        question = els[0].text.replace("−", "-").replace("×", "*").replace("÷", "/")
        question = re.sub("([0-9]+)([a-z])", "\\1*\\2", question)
      else:
        question = utils.parse_mathjax(els[0].elements(by.xpath("./*")))
      text = els[1].text
      name = text[0]
      value = re.search("[0-9]+", text).group(0)
      question = question.replace(name, value)
      answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    #except:
      #print("Error")
      i += 1

def solve_one_step():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=192", 
    1
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      els = s(".question-content").elements("p")[1].element("math")\
        .elements("mtd > mn, mtd > mo, mtd > msup, mtd > mfrac, mtd > mi, mtd > mrow")
      if els.size() == 0:
        els = s(".question-content").elements("p")[1]\
        .elements("math > mn, math > mo, math > msup, math > mfrac, math > mi, math > mrow")
      question = utils.parse_mathjax(els)
      lhs = re.search(".+(?==)", question).group(0)
      rhs = re.search("(?<==).+", question).group(0)
      equation = lhs + "-(" + rhs + ")"
      sp = sympy.parsing.sympy_parser.parse_expr(equation, transformations = "all")
      answer = sympy.solve(sp)[0]
      utils.answer_question(answer, questions_answered == 34, mq = True)
      questions_answered += 1
    #except:
      #print("Error")
      i += 1
