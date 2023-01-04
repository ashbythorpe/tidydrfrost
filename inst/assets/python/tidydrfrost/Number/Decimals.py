from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def place_value():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=177", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  s(".desmos, .maths-line, .ui-sortable").should(be.visible)
  
  while questions_answered < 35 and i < 100:
    #try:
      if ss(".desmos").size() > 0:
        question = s(".question-content").element("p")
        number = re.search("[0-9.]+", question.text).group(0)
        if number == ".":
          number = utils.execute_js("get_place_value_number")
          utils.answer_question(number, questions_answered)
        else:
          index = utils.execute_js(find_place_value_index, number)
          buttons = s(".answer-content").elements("input[type='radio']")
          buttons[index].click()
          s("input[type='submit']").click()
          utils.final_checks(questions_answered)
      elif ss(".ui-sortable").size() > 0:
        elements = s(".ui-sortable").elements("div")
        numbers = list(map(lambda x: float(x.text), elements))
        rank = sorted(range(len(numbers)), key=numbers.__getitem__)
        utils.execute_js("sort_by_rank", rank)
        s("input[type='submit']").click()
        utils.final_checks(questions_answered)
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
        buttons[index].click()
        s("input[type='submit']").click()
        utils.final_checks(questions_answered)
      questions_answered += 1
      s(".desmos, .maths-line, .ui-sortable").should(be.visible)
    #except:
    #  print("Error")
      i += 1

def decimal_addition_subtraction():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=177", 
    1
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    try:
      element = s(".question-content").elements("p")[1]
      question = element.text
      question = question.replace("−", "-")
      answer = round(eval(question), 8)
      utils.answer_question(answer, questions_answered)
      questions_answered += 1
    except:
      print("Error")
    i += 1
