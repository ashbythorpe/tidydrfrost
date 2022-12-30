from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def continue_sequence():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=191", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[0]
      numbers = re.findall("[-0-9]+", element.text)
      rel_numbers = list(map(lambda x: int(x), numbers[0:3]))
      last = int(numbers[-1])
      answer_boxes = s(".answer-content").elements("input")
      if rel_numbers[1] - rel_numbers[0] == rel_numbers[2] - rel_numbers[1]:
        # Arithmetic sequence
        diff = rel_numbers[1] - rel_numbers[0]
        answer = last + diff
        for el in answer_boxes[0:-1]:
          el.set(answer)
          answer += diff
      else:
        # Geometric sequence
        mult = rel_numbers[1]/rel_numbers[0]
        answer = last * mult
        for el in answer_boxes[0:-1]:
          el.set(answer)
          answer *= mult
      utils.answer_question(answer, questions_answered == 34, answer_input = answer_boxes[-1])
      questions_answered += 1
    except:
      print("Error")
      i += 1

def later_terms():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=191", 
    1
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      elements = s(".question-content").elements("p")
      numbers = re.findall("[-0-9]+", elements[1].text)
      rel_numbers = list(map(lambda x: int(x), numbers[0:3]))
      n = int(re.search("[0-9]+", elements[2].text).group(0))
      if rel_numbers[1] - rel_numbers[0] == rel_numbers[2] - rel_numbers[1]:
        # Arithmetic sequence
        diff = rel_numbers[1] - rel_numbers[0]
        answer = rel_numbers[0] + diff * (n - 1)
      else:
        # Geometric sequence
        mult = rel_numbers[1]/rel_numbers[0]
        answer = rel_numbers[0] * mult ** (n - 1)
      utils.answer_question(answer, questions_answered == 34)    
      questions_answered += 1
    except:
      print("Error")
      i += 1
