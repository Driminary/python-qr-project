===========
Version 1.0
===========
 Released:
11/03/2014
===========

=====
Files
=====
mod_imgtools.py 		- The module itself
required-python-modules.zip 	- The required python modules for the module to function
README.txt			- This file
LICENSE				- The MIT License file this module is released under
CHANGELOG.txt			- A text file containing the changes to this module
calibration_purewhite.png 	- A 100 x 100 px pure white image
calibration_25percent.png 	- The file above with a 50 x 50 px black square in the top left
	                          covering 25% of the image.

==================================================================================================
Requires: itertools [Included in python installation], Pillow 2.3.0 [Supplied]
==================================================================================================

A module to process an image of a QR code including the degredation of the image as well as the
compare() function to compare two equally sized images and find the percentage of pixels that are
different.

In this directory is a .zip file containing the win32 binaries for Pillow. Also included are two
png files for calibration and testing.

- calibration_purewhite.png = A 100 x 100 px pure white image
- calibration_25percent.png = The file above with a 50 x 50 px black square in the top left
                              covering 25% of the image.

For usage of each function, please refer to the DOCSTRING.

To embed this module in your code and for a simple encoding and decoding example, place the module
file (mod_imgtools.py) and the two calibration images in the same directory as your code and include
the following:

============== Copy below this line

# Thomas Anderson's (py12tja) Image Processing Module
import mod_imgtools

# Run compare function
print qr_imgtools.compare("calibration_purewhite.png","calibration_25percent.png")

# Run addblur function
qr_imgtools.addblur(10,"image.png")

============== Copy above this line

Remeber that due to the licensing this file is released under (MIT License), all usage must include
credit to the original owner (myself) and so you must include the first line if you import or it will
be an infringement of copyright.

Source files can be found on https://github.com/Driminary/python-qr-project