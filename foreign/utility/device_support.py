import pyaudio
import cv2

from desktopmagic.screengrab_win32 import getDisplayRects


def device_support(silent):
  device_obj = {'cams': 0}

  try:
    device_obj['monitors'] = len(getDisplayRects())
  except:
    device_obj['monitors'] = '???'

  if silent:
    device_obj['cams'] = '???'
  else:
    while True:
      cam = cv2.VideoCapture(device_obj['cams'])
      check, frame = cam.read()
      if not check:
        break
      device_obj['cams'] += 1

  try:
    pyaudio.PyAudio().get_default_input_device_info()
  except:
    device_obj['microphone'] = False
  else:
    device_obj['microphone'] = True
  
  return device_obj