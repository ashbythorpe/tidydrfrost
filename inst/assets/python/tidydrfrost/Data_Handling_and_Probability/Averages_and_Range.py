from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import sigfig
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def mean():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=171", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      element = s(".question-content").elements("p")[1]
      numbers = list(map(lambda x: int(x), re.findall("[0-9]+", element.text)))
      answer = sigfig.round(sum(numbers)/len(numbers), decimals = 1)
      answer
      utils.answer_question(answer, questions_answered)
      questions_answered += 1
    #except:
    #  print("Error")
      i += 1
