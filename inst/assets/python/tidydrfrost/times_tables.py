from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def times_tables_iter():
  robust.get_with_retry(
    "https://www.drfrostmaths.com/timestables-game.php",
    "#question"
  )
  
  s("#question").element("a").click()
  question_el = s("#question")
  answer_box = s("#calculator-display")
  
  for i in range(100):
    try:
      question = question_el.text
      question = question.replace("×", "*")
      question = question.replace("÷", "/")
      answer = round(eval(question))
      answer_box.set(answer)
    except:
      print("Error")

def times_tables_game(driver, n):
  robust.get_with_retry(
    "https://www.drfrostmaths.com/timestables-game.php?id=" + str(n),
    "#question"
  )
  driver.get("https://www.drfrostmaths.com/timestables-game.php?id=" + str(n))
  s("#question").element("a").click()
  answer_box = s("#calculator-display")
  
  for i in range(40):
    try:
      question_el = s("#question")
      if n == 4:
        # Powers
        power_el = question_el.element("sup")
        relevant_question = question_el.text[0:-1]
        question = relevant_question + " ** " + power_el.text
        answer = round(eval(question))
      elif n == 28:
        # Square numbers
        x = eval(question_el.text[0:-1])
        answer = x * x
      elif n == 29:
        # Cube numbers
        x = eval(question_el.text[0:-1])
        answer = x * x * x
      else:
        question = question_el.text
        question = question.replace("×", "*")
        question = question.replace("÷", "/")
        answer = round(eval(question))
      answer_box.set(answer)
    except:
      print("Error")
