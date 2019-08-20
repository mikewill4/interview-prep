# Sockets
* End point of communication
* Message must traverse underlying network
* Messages can go in and out of sockets
## Ports
* Destination port uniquely identifies a socket to use
* 16-bit quantity
* Common ports:
	* 22 (ssh)
	* 23 (ftp)
	* 25 (email)
	* 80 (http)
	* 443 (https)
* Well known ports are between 0-1023
* Unused ephemeral (temporary) ports are between 20124-65535
## Creating a socket
* int socket(int domain, int type, int protocol)
* Domain: protocol family
* Type: semantics of communication
	* SOCK_STREAM: reliable byte stream
	* SOCK_DGRAM: message-oriented service
* Protocol: specific protocol
	* UNSPEC: unspecified
	* SOCK_STREAM implies TCP for example
## Connecting socket to server
* Translate hostname to IP address
* Identify service's port number using service name and protocol
* Establish connection
