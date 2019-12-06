import os

from domestic.utility.read_file import *
from domestic.global_state import *


def alias_parser(data):
  if os.path.isfile(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/alias.txt'):
    aliases = read_file(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/alias.txt').decode(state['settings']['encoding']).strip().split('\n')

    for alias in aliases:
      key, value = alias.split('=')
      if data == key:
        return value
    
  return data