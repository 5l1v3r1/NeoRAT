import pyaudio

from domestic.global_state import *


def get_io_channels():
  try:
    p = pyaudio.PyAudio()
  except:
    pass
  else:
    try:
      state['settings']['io-channels'][0] = str(p.get_default_input_device_info()['maxInputChannels'])
    except:
      pass
    
    try:
      state['settings']['io-channels'][1] = str(p.get_default_output_device_info()['maxOutputChannels'])
    except:
      pass