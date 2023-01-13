from selene import browser, be
from selene.api import s

def click(elem):
  driver = browser.driver()
  elem.should(be.visible)
  driver.execute_script(
    "$(arguments[0]).click()", elem.get_actual_webelement()
  )

def input_set(elem, value):
  driver = browser.driver()
  elem.should(be.visible)
  driver.execute_script(
    "$(arguments[0]).val(arguments[1])", elem.get_actual_webelement(), value
  )

def mq_set(elem, value):
  driver = browser.driver()
  elem.should(be.visible)
  driver.execute_script(
    "var MQ = MathQuill.getInterface(2); MQ(arguments[0]).latex('').typedText(arguments[1])", 
    elem.get_actual_webelement(), str(value)
  )

def execute_js(function, *args, **kwargs):
  temp_names = list(map(lambda x: "_temp" + str(x), range(len(args))))
  statements = list(map(lambda x, y: f"let {x} = arguments[{str(y)}]", temp_names, range(len(args))))
  unnamed = ",".join(temp_names)
  
  names = list(kwargs.keys())
  name_statements = list(map(lambda x, y: f"let {x} = arguments[{str(y + len(args))}]", names, range(len(kwargs))))
  named = ",".join(map(lambda x: f"{x} = {x}", names))
  
  if unnamed == "" or named == "":
    final = "".join([unnamed, named])
  else:
    final = ",".join([unnamed, named])
  
  function_statement = f"let {function} = eval('(' + window.localStorage.getItem('{function}') + ')')"
  setup = ";".join([function_statement, *statements, *name_statements])
  
  driver = browser.driver()
  return driver.execute_script(setup + "; return " + function + "(" + final + ");", *args, *kwargs.values())
