from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import sigfig
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust
from tidydrfrost.decorators import task

@task("explorer.php?noid=171", 0)
def mean(questions_answered):
  element = s(".question-content").elements("p")[1]
  numbers = list(map(lambda x: int(x), re.findall("[0-9]+", element.text)))
  answer = sigfig.round(sum(numbers)/len(numbers), decimals = 1)
  utils.answer_question(answer, questions_answered)
