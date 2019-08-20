# Client-Server model
## Client
* Sometimes on
* Typically the human end user
* Connects to the server and makes some sort of request
* Receives a response
### Typical client program
* Prepare to communicate
	* Create a socket
	* Determine server address and port number
	* Initiate connection to server
* Exchange data with the server
	* Write data to socket
	* Read data from socket
	* Do stuff with data
* Close the socket
## Server
* Always on
* Fulfills requests from many clients
* Fixed, well-known address
