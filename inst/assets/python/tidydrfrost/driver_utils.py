from selene import browser, by, config
from selene.api import s, ss
from time import sleep
import re
from tidydrfrost.robust_utils import get_with_retry
import tidydrfrost.js_utils as js
from os import walk

def end_session():
  sleep(2)
  
  browser.close()

def login(eml, pwd):
  config.base_url = "https://www.drfrostmaths.com/"
  config.timeout = 10
  
  get_with_retry(
    "login.php",
    by.name("login-email")
  )
  
  js.input_set(s(by.name("login-email")), eml)
  
  js.input_set(s(by.name("login-password")), pwd)
  
  js.click(s("#login-submit-button"))
  
  modals = ss(".modal")
  if modals.size() > 0:
    return False
  
  return True

def get_points():
  points_text = s(".taskcomplete").elements("p")[0]
  points = int(re.search("[0-9]+", points_text.text).group(0))
  return points

def source_js(file):
  driver = browser.driver()
  driver.execute_script(open(file).read())

def source_all_js(path):
  files = []
  for (dirpath, dirnames, filenames) in walk(path):
    files.extend(map(lambda file: dirpath + "/" + file, filenames))
  js_files = filter(lambda x: re.search(".js$", x) != None, files)
  list(map(source_js, js_files))
  
