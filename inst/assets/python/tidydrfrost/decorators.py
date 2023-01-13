from functools import wraps
from selene import browser
from selene.api import s, ss
import tidydrfrost.utils as utils
import tidydrfrost.robust_utils as robust

def task(url, n):
  def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        utils.start_task(url, n)
        
        questions_answered = 0
        cum_errors = 0
  
        while questions_answered < 35 and cum_errors < 5:
          try:
            if ss(".taskcomplete").size() > 0:
              break
            f(*args, **kwds, questions_answered = questions_answered)
            questions_answered += 1
            cum_errors = 0
          except Exception as e:
            if ss(".taskcomplete").size() > 0:
              break
            last_error = e
            robust.close_modals()
            try:
              utils.final_checks()
              questions_answered += 1
            except:
              pass
            if cum_errors == 2:
              browser.driver().refresh()
            cum_errors += 1
        if cum_errors >= 5:
          raise last_error
    return wrapper
  return decorator
