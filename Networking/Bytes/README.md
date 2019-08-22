# Bytes
## Endianness
* Little endian
	* "little end comes first"
	* Intel PCs
	* Low-order byte stored at lowest memory location
	* Ex: byte0, byte1, etc.
* Big endian
	* "big end comes first"
	* High-order byte stored at lowest memory location
	* Ex: byte3, byte2, etc.
* Sockets don't typically handle endianness differences
	* They don't know the data types
	* Only see data as a buffer pointer and length
