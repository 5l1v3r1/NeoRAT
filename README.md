## Alvin
Free, open-source remote access tool for windows

### Description
Alvin is an open-source TCP application protocol used to control multiple computers transfering requested data over to the server without interference by the client user. Supporting large amount of features with a whide range of options. Alvin demonstrates the possibilities of python used in conjunction with other open-source projects.

* The server script is supported cross platform
* The client script is supported for windows

### Features
* TCP Network Stream (IPv4)
* Deflate Compression & AES128 Encryption
* Automatic Documentation
* Stable Remote Shell
* Desktop Stream (Multi Monitor)
* Cam Stream (Multi Monitor)
* Audio Listener (Mic & Loopback Audio)
* Audio Output
* Keylogger
* Screenshot
* Cam Screenshot
* Upload (Execute)
* Download (Execute)
* File Encryption / Decryption
* Keystroke Injection
* Mouse Action Injection
* Python Interpreter (Print Result to Server)
* Keyboard & Mouse Lock / Unlock
* Password Recovery ([LaZagne Project](https://github.com/AlessandroZ/LaZagne))
* Privilege Escelation
* Clearing Windows Logs
* Show Messagebox
* Open Websites
* System Actions
  * Shutdown
  * Restart
  * Logout
  * Standby

### Running Alvin
Simply install all neccesary python packages in ~build/requirements folder

Running server.py:
* __python server.py__  -ip [server IP] -p [server port]<br>
* Optionally you can specify IP & port of server. Default IP: localhost | Default port: 1200.

Running client.py:
* __python client.py__ -ip [server IP] -p [server port]<br>
* Optionally you can specify IP & port of host server. Default IP: localhost | Default port: 1200.

### Known Issues
* Threaded commands may silently fail. These consist of all modules (stream, cam stream, audio & talk), keylogger & keystroke.
* Using "unbind" for modules may leave sockets alive because of slow updating, if this happens use "close [index]".
* Audio & talk modules support either 1 or 2 audio channels, but if server & client doesn't have the same number of channels the sound may appear distorted.


_Please don't use Alvin for illegal purposes_