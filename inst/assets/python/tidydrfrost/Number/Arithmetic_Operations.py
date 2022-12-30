from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import math
import sigfig
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def addition_subtraction():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[1]
      question = element.text
      question = question.replace("−", "-")
      answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1

def multiplication():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    2
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[1]
      question = element.text
      question = question.replace("×", "*")
      answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1

def pictoral_division():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    3
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").element("p")
      question = re.search("[0-9]+.[0-9]+", element.text).group(0)
      question = question.replace("÷", "/")
      answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1

def division():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    4
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[1]
      question = element.text
      answer_boxes = s(".answer-content").elements("input")
      if answer_boxes.size() == 1:
        try:
          question = question.replace("÷", "/")
          answer = eval(question)
        except:
          elem0 = s(".question-content").elements("p")[0]
          question = elem0.text + element.text
          numbers = re.findall("[0-9]+", question)
          n1 = int(numbers[0])
          n2 = int(numbers[1])
          if n1 >= n2:
            answer = n1/n2
          else:
            answer = n2/n1
          answers = [math.floor(answer), math.ceil(answer)]
          utils.try_two_answers(answers, questions_answered == 34)
          questions_answered += 1
          continue
        utils.answer_question(answer, questions_answered == 34)
        questions_answered += 1
      elif answer_boxes.size() == 2:
        numbers = re.findall("[0-9]+", question)
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        answer_boxes[0].set(n1 // n2)
        utils.answer_question(n1 % n2, questions_answered == 34, answer_boxes[1])
        questions_answered += 1
      else:
        numbers = re.findall("[0-9]+", question)
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        answer_boxes[0].set(n1 // n2)
        answer_boxes[1].set(n1 % n2)
        utils.answer_question(n2, questions_answered == 34, answer_boxes[2])
        questions_answered += 1
    except:
      print("Error")
    i += 1

def number_facts():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    7
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[3]
      question = element.text
      question = question.replace("−", "-")
      question = question.replace("×", "*")
      question = question.replace("÷", "/")
      answer = round(eval(question), 8) # For thirds
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1

def missing_digits():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    9
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      text = s(".question-content").elements("p")[1].text
      numbers = re.findall("[0-9]+", text)
      incomplete = map(lambda x: len(x) < 3, numbers)
      missing = {}
      for ida, a in enumerate(incomplete):
        if a:
          row = s(".question-content").element("math").elements("mtr")[ida]
          elements = row.elements("mn, menclose")
          x = list(map(lambda x: x.tag_name == "menclose", elements)).index(True)
          missing[ida] = x
      adjusted_numbers = []
      for idb, b in enumerate(numbers):
        if idb in missing.keys():
          position = missing[idb]
          adjusted = b[:position] + "0" + b[position:]
        else:
          adjusted = b
        adjusted_numbers.append(int(adjusted))
      sign = s(".question-content").element("math").elements("mtr")[1].\
        element("mo").text
      if sign != "+":
        adjusted_numbers[1] = -adjusted_numbers[1]
      adjusted_numbers[2] = -adjusted_numbers[2]
      total = -sum(adjusted_numbers)
      divide = 0
      for b, a in missing.items():
        if b == 2 or (b == 1 and sign != "+"):
          divide -= (10 ** (2-a))
        else:
          divide += (10 ** (2-a))
      if divide == 0:
        # Unanswerable question, answer can be between [0-4]
        utils.try_two_answers([0, 1], questions_answered == 34)
        questions_answered += 1
      else:
        answer = total/divide
        utils.answer_question(answer, questions_answered == 34)
        questions_answered += 1
    except:
      print("Error")
    i += 1

def bidmas():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    10
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      if s(".question-content").elements("p")[1].elements("msup").size() == 0:
        element = s(".question-content").elements("p")[1]
        question = element.text
        question = question.replace("−", "-")
        question = question.replace("×", "*")
        question = question.replace("÷", "/")
        answer = eval(question)
      else:
        if s(".question-content").elements("p")[1].elements("mrow").size() == 0:
          elements = s(".question-content").elements("p")[1]\
            .elements("mtd > mn, mtd > mo, mtd > msup")
        else:
          elements = s(".question-content").elements("p")[1]\
            .elements("math > mn, math > mo, math > msup, math > mrow")
        question = utils.parse_mathjax(elements)
        answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1

def estimate_calculations():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=175", 
    11
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      if s(".question-content").elements("p")[1].elements("mfrac").size() == 0:
        question = s(".question-content").elements("p")[1].text
        n1, n2 = re.findall("[0-9.]+", question)
        final = question.replace(n1, str(sigfig.round(float(n1), sigfigs = 1)))\
          .replace(n2, str(sigfig.round(float(n2), sigfigs = 1)))\
          .replace("−", "-").replace("×", "*")
        answer = eval(final)
      else:
        fraction = s(".question-content").elements("p")[1].element("mfrac")
        num = fraction.element("mrow").text
        denom = fraction.element("mfrac > mn").text
        n1, n2 = re.findall("[0-9.]+", num)
        final_num = num.replace(n1, str(sigfig.round(float(n1), sigfigs = 1)))\
          .replace(n2, str(sigfig.round(float(n2), sigfigs = 1)))\
          .replace("−", "-").replace("×", "*")
        answer = eval(final_num) / sigfig.round(float(denom), sigfigs = 1)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1
