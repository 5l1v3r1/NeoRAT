from domestic.utility.status_message import *
from domestic.utility.get_timestamp import *
from domestic.global_state import *


def delete_client(client, write_stdout=True, notifications=True):
  state['sockets']['clients'][0][client].close()
  state['sockets']['clients'][0][client] = None
  
  username = state['sockets']['clients'][2][client]['username']
  if state['options']['information-gathering']['history']:
    with open(f'{state["root"]}/{username}/history.txt', 'a') as f:
      f.write(f'{username} disconnected at {get_timestamp()}\n')

  for index, item in enumerate(state['sockets']['clients']):
    del state['sockets']['clients'][index][client]

  if write_stdout:
    status_message('Client successfully deleted', 'success')
  elif state['options']['notices']['notice'] and notifications:
    state['settings']['notifier'].show_toast('Disconnection Notice!', f'Username: {username}', duration=4)