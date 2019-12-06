import os

from domestic.parse.internal_server_error_exception_handling import *
from domestic.parse.command_argument_parser import *
from domestic.parse.command_validation import *
from domestic.utility.program_setup import *
from domestic.parse.alias_parser import *
from domestic.global_state import *


@internal_server_error_exception_handling
def main():
  state['root'] = '{}/aftermath'.format(os.getcwd().replace('\\', '/'))
  program_setup()

  while True:
    data = command_argument_parser(alias_parser(input()))
    command_validation(data)


if __name__ == '__main__':
  main()