from selene import browser, be
from selene.api import s, ss
import time
from time import sleep

def get_with_retry(url, selector):
  current_retry = 0
  while current_retry < 4:
    browser.open_url(url)
    try:
      s(selector).should(be.visible)
      return True
    except:
      pass
    current_retry += 1
  raise TimeoutError("Page could not be visited.")

def close_modals():
  while ss(".modal").size() > 0:
    if s(".modal").elements(".taskcomplete").size() > 0:
      break
    else:
      s(".close-modal").click()
