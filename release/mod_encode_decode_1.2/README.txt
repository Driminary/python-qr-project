===========
Version 1.2
===========
 Released:
12/02/2014
===========

=====
Files
=====
mod_encode_decode.py 		- The module itself
required-python-modules.zip 	- The required python modules for the module to function
README.txt			- This file
LICENSE				- The MIT License file this module is released under
CHANGELOG.txt			- A text file containing the changes to this module

==================================================================================================
Requires: qrcode 4.0.4, zbar 0.10, Pillow 2.3.0 [Supplied for windows systems]
==================================================================================================

A module to generate a QR code from a user inputted string, as well as decode a given image file to
determine if it is a QR code and what the message is.

In this directory is a .zip file containing the win32 binaries for PIL and zbar and the source files
for qrcode.

For usage of each function, please refer to the DOCSTRING.

To embed this module in your code and for a simple encoding and decoding example, place the module
file (mod_encode_decode.py) in the same directory as your code and include the following:

============== Copy below this line

# Thomas Anderson's (py12tja) Encoding Decoding Module
import mod_encode_decode

# Run encoding module
mod_encode_decode.encode("Random Message","code")

# Run decoding module
mod_encode_decode.decode("code.png")

============== Copy above this line

Remeber that due to the licensing this file is released under (MIT License), all usage must include
credit to the original owner (myself) and so you must include the first line if you import or it 
will be an infringement of copyright.

Source files can be found on https://github.com/Driminary/python-qr-project