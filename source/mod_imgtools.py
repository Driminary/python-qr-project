# -*- coding: utf-8 -*-
# @author: Thomas Anderson
 
###################
# mod_imgtools.py #
###################
# Thomas Anderson #
###################
#    30/01/2014   #
###################
#  Last updated:  #
#    30/01/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#    Image Processing    #
#         Module         #
##########################

"""

===========
Version 0.1
===========
 Released:
00/00/0000
===========

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

============== Copy above this line

Remeber that due to the licensing this file is released under (MIT License), all usage must include
credit to the original owner (myself) and so you must include the first line if you import or it will
be an infringement of copyright.

Source files can be found on https://github.com/Driminary/python-qr-project

"""

################
# Begin Module #
################

# If module is being run on its own, not imported as a module, exit gracefully.
if __name__ == '__main__':
    print "Please import the module rather than run it standalone. (See file for details)"
    raise RuntimeError
    
# Import required modules
from itertools import izip
from PIL import Image

###################
# Begin Functions #
###################

# Define compare()
def compare(image_1,image_2):
    
    """
    
    Image Compare Function
    ======================
    
    Compares two specified image files of equal size and finds the percentage of pixels that differ. Returns
    that percentage number.
    
    Arguments:
    ----------
    
    image_1  - The first image file name to compare [MUST be a string]
    image_2  - The second image file name to compare [MUST be a string]
    
    Returns:
    --------
    
    percentdiff - A float of the percentage difference in the pixels between the two images
    
    Usage: 
    ------
    
    compare("img1.png","img2.png") - Compares img1.png to img2.png and finds the difference in their pixels
    
    """
    
    # Open both images and covert to greyscale
    try:
        i1 = Image.open(image_1).convert('L')
        i2 = Image.open(image_2).convert('L')
    except:
        # Image file is not an image
        print "Sorry, one or both of the files provided was not an image."
        raise TypeError    

    # Make sure images are compatible to be compared
    assert i1.mode == i2.mode, "Images are not compatible for comparison (Image types are different)"
    # Make sure images are of same size    
    assert i1.size == i2.size, "Images are different sizes"
    
    # Zip pixel data for both images together
    pairs = izip(i1.getdata(), i2.getdata())
    dif = sum(abs(p1-p2) for p1,p2 in pairs) # Subtract to find the difference between the two corresponding pixels
    
    ncomponents = i1.size[0] * i1.size[1] # Total number of pixels in image
    
    # Set the percentage difference as the difference in each pixel (divided by the 255 greyscale scale), times 100%,
    # divided by the total pixel count
    percentdiff = (dif / 255.0 * 100) / ncomponents
    
    # Return the difference
    return percentdiff
    
#################
# End Functions #
#################

##############
# End Module #
##############