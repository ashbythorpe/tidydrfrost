from selene import browser, by, be, have
from selene.api import s, ss
from time import sleep
import re
import sigfig
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def pictograms():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=172", 
    0
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      rows = s(".question-content").element("tbody").elements("tr")
      key = s(".question-content").elements("p")[2].text
      mult = int(re.search("[0-9]+", key).group(0))
      answers = []
      
      if mult == 2:
        for row in rows:
          pictures = row.elements(".qimg-wrapper")
          if pictures.size() > 1:
            large_size = pictures[0].rect["width"]
            break
        else:
          large_size = 30
        for row in rows:
          pictures = row.elements(".qimg-wrapper")
          if pictures[-1].rect["width"] < large_size:
            answers.append((pictures.size() - 1/2) * mult)
          else:
            answers.append(pictures.size() * mult)
      else:
        width_map = {
          24: 1/4,
          25: 1/2,
          37: 3/4,
          36: 1
        }
        for row in rows:
          pictures = row.elements(".qimg-wrapper")
          final_width = pictures[-1].rect["width"]
          answers.append((pictures.size() - 1 + width_map[final_width]) * mult)
      utils.multiple_answers(answers, questions_answered)
      questions_answered += 1
    #except:
    #  print("Error")
      i += 1

def bar_charts():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=172", 
    1
  )
  
  driver = browser.driver()
  
  questions_answered = 0
  i = 0
  
  s(".desmos-calculator, .desmos").should(be.visible)
  
  while questions_answered < 35 and i < 100:
    #try:
      if ss(".desmos-calculator").size() > 0:
        to_ignore = utils.execute_js("bar_to_ignore")
      
        nums = s(".question-content").element("table").elements("td")
        values = list(map(lambda x: int(x.text), nums))
        values.pop(to_ignore)
        utils.execute_js("set_expressions", values)
        
        s("input[type='submit']").click()
        utils.final_checks(questions_answered)
      else:
        values = utils.execute_js("get_bar_values")
        to_find = s(".question-content").elements(by.xpath("./p"))[3].text
        x_axis = list(map(lambda x: x.text, s(".question-content").elements(".dcg-label")))
        count = list(map(lambda x: to_find.count(x), x_axis))
        
        if not all(map(lambda x: x == 0, count)):
          index_max = max(range(len(count)), key=count.__getitem__)
          answer = values[index_max]
        else:
          # Assume total
          x_nums = map(lambda x: int(x), x_axis)
          totals = map(lambda x, y: x * y, x_nums, values)
          answer = sum(totals)
        utils.answer_question(answer, questions_answered)
      questions_answered += 1
      s(".desmos-calculator, .desmos").should(be.visible)
    #except:
    #  print("Error")
      i += 1

def bank_statements():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=172", 
    3
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      input_row = s(".tableinput").element("input").element(by.xpath("./parent::td/parent::tr"))
      current = float(re.search("[0-9.]+", input_row.elements("td")[-1].text).group(0))
      previous = input_row.elements(by.xpath("./preceding-sibling::tr"))[-1]
      search = re.search("[0-9.]+", previous.elements("td")[-1].text) 
      if search == None:
        answer = abs(current)
      else:
        prev = float(search.group(0))
        answer = sigfig.round(abs(current - prev), decimals = 1)
      utils.answer_question(answer, questions_answered)
      questions_answered += 1
    #except:
    #  print("Error")
      i += 1

def pie_charts():
  utils.start_task(
    "https://www.drfrostmaths.com/explorer.php?noid=172", 
    4
  )
  
  questions_answered = 0
  i = 0
  
  while questions_answered < 35 and i < 100:
    #try:
      if s(".answer-content").elements("table").size() > 0:
        total_text = s(".question-content").element("p").text
        total = int(re.search("[0-9]+", total_text).group(0))
        rows = s(".answer-content").element("table").elements("tr")
        items = map(lambda el: el.elements("td")[1].text, rows)
        numbers = map(int, list(items)[1:])
        answers = map(lambda x: sigfig.round(x/total * 360, decimals = 0), numbers)
        utils.multiple_answers(list(answers), questions_answered)
      else:
        total_text = s(".question-content").element("p").text
        total = int(re.search("[0-9]+", total_text).group(0))
        elements = s(".desmos").elements(".dcg-label")
        elements.should_not(have.size(0))
        elements.should_each(be.visible)
        elements.should_each_not(have.exact_text(''))
        texts = list(map(lambda x: x.text, elements))
        keys = texts[1::2]
        values = list(map(lambda x: int(x.replace("º", "")), texts[::2]))
        question = s(".question-content").elements(by.xpath("./p"))[3].text
        regex = "(" + "|".join(keys) + ")"
        key = re.search(regex, question).group(0)
        index = keys.index(key)
        angle = values[index]
        answer = angle/360 * total
        utils.answer_question(answer, questions_answered)
      questions_answered += 1
    #except:
    #  print("Error")
      i += 1
