from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import math
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
    #try:
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
    #except:
    #  print("Error")
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
      answer = eval(question)
      utils.answer_question(answer, questions_answered == 34)
      questions_answered += 1
    except:
      print("Error")
    i += 1
