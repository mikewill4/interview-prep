# Protocols
## File Transfer Protocol (FTP)
* Allow user to copy files to/from remote hosts
* Requires users to know name of server machine, have an account, and know where files are stored
* Port 21 (on server)
## HTTP
* Server repsonse codes
	* 1XX: positive preliminary reply
	* 2XX: positive completion reply
	* 3XX: positive intemediary reply
	* 4XX: transient negative completion reply
	* 5XX: permanent negative completion reply
## Out-of-band control
* Characteristic of network protocols
* Pass control data (username, password, etc.) on a separate connection from main data
* Useful for when data transfer is aborted or when a third-party file transfer is between two hosts
