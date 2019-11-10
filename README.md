# Neo
![Neo](https://github.com/Alvin-22/Neo/blob/master/~build/images/Neo.PNG "Available commands in Neo")

## Context
Neo is two scripts used seperately, but work together transfering data over TCP sockets. The server script manages all the connections made from clients, when a client connects to the server the client can be seen by the server, interacted with & controled. Neo has two modes, shell & session. Shell is simply to manage clients in an overview manner, while session is interacting specifically with Z client. An active session means a reverse shell & access to all session specific commands.

Simply globally available commands are used for control on the program level, shell commands are for client management level & session commands are on a client specific level.

## Running Neo
Simply install all neccesary python packages in ~build/requirements folder

Running server.py:
* python server.py -b -ip [server IP] -p [server port]
The server.py script has three flags available. "-b" flag binds all sockets & make it really easy to proceed, automatically listens for clients, "-ip" can be used to specify your servers IP with being localhost as default. "-p" flag will specify what port you want to listen on, by default port 1200 is used.

Running client.py:
* python client.py -ip [server IP] -p [server port]
The client script is abit easier, you can specify the IP & port of the server you're running server.py from. By default the ip is localhost & port is 1200.
