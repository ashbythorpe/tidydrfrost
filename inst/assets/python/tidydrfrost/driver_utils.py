from selene import browser, by, config
from selene.api import s, ss
from time import sleep
import re
from tidydrfrost.robust_utils import get_with_retry

def end_session():
  sleep(2)
  
  browser.close()

def login(eml, pwd):
  config.timeout = 10
  
  get_with_retry(
    "https://www.drfrostmaths.com/login.php",
    by.name("login-email")
  )
  
  s(by.name("login-email")).set(eml)
  
  s(by.name("login-password")).set(pwd)
  
  s("#login-submit-button").click()
  
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
  
