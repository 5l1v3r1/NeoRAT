import multiprocessing
import win32con
import win32gui
import time

from foreign.utility.terminal_pipe import *


def standby_action():
  win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, 0xF170, 2)


def system(action_type, extra_data):
  if action_type == 'shutdown':
    return {'message': terminal_pipe('shutdown /p /f', extra_data[0], extra_data[1])}
  elif action_type == 'restart':
    return {'message': terminal_pipe('shutdown /r /f /t 0', extra_data[0], extra_data[1])}    
  elif action_type == 'logout':
    return {'message': terminal_pipe('shutdown /l /f', extra_data[0], extra_data[1])}    
  elif action_type == 'standby':
    standby_thread = multiprocessing.Process(target=standby_action, daemon=True)
    standby_thread.start()
    time.sleep(5)
    standby_thread.terminate()
    return {'message': 'Successfully activated standby mode', 'text_mode': 'success'}
  else:
    raise Exception('Error message')