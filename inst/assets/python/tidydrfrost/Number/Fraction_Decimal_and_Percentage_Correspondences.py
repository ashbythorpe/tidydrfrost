from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import sympy
import re
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def conversion():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=179", 
    0
  )
  
  driver = browser.driver()
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      s(".question-content")\
        .element(by.xpath('./p[position() = 2]|.//div[@class = "desmos"]'))\
        .should(be.visible)
      if s(".question-content").elements(".desmos").size() > 0:
        answer = utils.execute_js("get_filled_percentage")
        utils.answer_question(answer, questions_answered)
      else:
        if s(".question-content").elements("p")[1].elements("mfrac").size() > 0:
          input_type = "fraction"
        elif "%" in s(".question-content").elements("p")[1].text:
          input_type = "percentage"
        else:
          input_type = "decimal"
        out_as = s(".question-content").elements("p")[2].text
        output_type = re.search("(fraction|decimal|percentage)", out_as).group(0)
        if input_type == "fraction":
          fraction = s(".question-content").elements("p")[1].element("mfrac")
          els = fraction.elements("mn")
          if output_type == "decimal":
            answer = round(int(els[0].text)/int(els[1].text), 8)
            utils.answer_question(answer, questions_answered)
          else:
            answer = round(int(els[0].text)/int(els[1].text) * 100, 8)
            utils.answer_question(answer, questions_answered)
        elif input_type == "decimal":
          decimal = s(".question-content").elements("p")[1].text
          if output_type == "fraction":
            fraction = sympy.core.sympify(decimal, rational = True)
            utils.multiple_answers([fraction.p, fraction.q], questions_answered)
          else:
            answer = round(float(decimal) * 100, 8)
            utils.answer_question(answer, questions_answered)
        else:
          percentage = s(".question-content").elements("p")[1].text.replace("%", "")
          if output_type == "fraction":
            answer = round(float(percentage) / 100, 8)
            utils.answer_question(answer, questions_answered)
          else:
            decimal = percentage + "/" + "100"
            fraction = sympy.core.sympify(decimal, rational = True)
            utils.multiple_answers([fraction.p, fraction.q], questions_answered)
      questions_answered += 1
    #except:
    #  print("Error")
      i += 1





