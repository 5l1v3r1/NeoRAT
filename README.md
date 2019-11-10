## Neo
Free, open-source remote administration tool for windows

### Description
Neo is an open-source project used to control multiple computers transfering requested data over to the server from clients without interference by the client user. Supporting large amount of features with a whide range of possibilities. Neo demonstrates the possibilities of python used in conjunction with other open-source projects. 

![Neo](https://github.com/Alvin-22/Neo/blob/master/~build/images/Neo.PNG "Available commands in Neo")

### Running Neo
Simply install all neccesary python packages in ~build/requirements folder

Running server.py:
* __python server.py__ ARGUMENTS: __-b -ip [server IP] -p [server port]__<br>
The server.py script has three flags available. "-b" flag binds all sockets & make it really easy to proceed, automatically listens for clients, "-ip" can be used to specify your servers IP with being localhost as default. "-p" flag will specify what port you want to listen on, by default port 1200 is used.

Running client.py:
* __python client.py__ ARGUMENTS: __-ip [server IP] -p [server port]__<br>
The client script is abit easier, you can specify the IP & port of the server you're running server.py from. By default the ip is localhost & port is 1200.

_Please don't use Neo for illegal purposes_
