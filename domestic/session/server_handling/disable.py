from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *


@error_exception_handling
def disable(message):
  unlock = validate_dict_key(message, 'unlock')

  if unlock is None:
    message['unlock'] = False

  session_message(message)