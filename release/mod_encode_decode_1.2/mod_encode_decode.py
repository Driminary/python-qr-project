# -*- coding: utf-8 -*-
# @author: Thomas Anderson
 
########################
# mod_encode_decode.py #
########################
# Thomas Anderson #
###################
#    30/01/2014   #
###################
#  Last updated:  #
#    12/02/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#   Encoding/Decoding    #
#        Module          #
##########################

"""

===========
Version 1.2
===========
 Released:
12/02/2014
===========

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

"""

################
# Begin Module #
################

# If module is being run on its own, not imported as a module, exit gracefully.
if __name__ == '__main__':
    print "Please import the module rather than run it standalone. (See file for details)"
    raise RuntimeError
    
# Import required modules
import qrcode
import zbar
from PIL import Image

###################
# Begin Functions #
###################

# Define encode()
def encode(raw_message,image_name,size=1,error=2): # Set default image size to 1 and up to 15% redundancy

    """
    
    QR Encoding Function
    ====================
    
    Generates a QR code image containing a specified message and outputs it to a specified image file. 
    Also contains options to set the size and error redundancy options.
    
    Arguments:
    ----------
    
    raw_message - The message to be encoded in the QR code. [MUST be a string]
    image_name  - The name of the image file produced, i.e. image_name.png [MUST be a string]
    size        - The size of the QR code, can be any integer between 1 and 40
    error       - The error redundancy, can be either 1,2,3 or 4. [Corresponds to 7,15,25 and 30% redundancy]
    
    Returns:
    --------
    
    Nothing
    (An image file with name image_name.png is created with the encoded message)
    
    Usage: 
    ------
    
    encode("Random Message","code") - Generates a QR code with message "Random Message" and
                                      puts it in 'code.png'. Uses default size (1) and error 
                                      redundancy (15%).
    
    """
    
    # Check the error redundancy is an accepted value.
    if error == 1:
        error_correct = qrcode.constants.ERROR_CORRECT_L # Up to 7% error redundancy
    elif error == 2:
        error_correct = qrcode.constants.ERROR_CORRECT_M # Up to 15% error redundancy [Default]
    elif error == 3:
        error_correct = qrcode.constants.ERROR_CORRECT_Q # Up to 25% error redundancy
    elif error == 4:
        error_correct = qrcode.constants.ERROR_CORRECT_H # Up to 30% error redundancy
    else:
        # Raise a ValueError if it isn't an accepted value
        print "Sorry an incorrect error redundancy was provided."
        raise ValueError

    # Check the size is an accepted value (Between 1 and 40)
    if size > 40 or size < 1:
        # Raise a ValueError if it isn't an accepted value
        print "Sorry an incorrect image size was provided."
        raise ValueError
        
    # Check the message to be encoded is a string
    try:
        str(raw_message)
    except:
        # Raise a ValueError if it isn't a string
        print "Sorry an incorrect message was provided."
        raise ValueError
        
    # Check the image file name is a string
    try:
        str(image_name)
    except:
        # Raise a ValueError if it isn't a string
        print "Sorry an incorrect image name was provided."
        raise ValueError
        
    # Generate the QR Code, code adapted from the qrcode source website
    qr = qrcode.QRCode(
        version=size, # Set the size of the image from the arguments
        error_correction=error_correct, # Set the appropriate error redundancy
        box_size=10, # Leaving this as default
        border=4, # Leaving this as default
        )
        
    # Add the message
    qr.add_data(raw_message)
        
    # Create the QR code data
    qr.make(fit=True)

    # Generate an image of the QR code data
    f = qr.make_image()
    
    # Save image
    f.save("%s.png" % image_name)
        
    return
    
# Define decode()
def decode(image_file):
    
    """
    
    QR Decoding Function
    ====================
    
    Reads a specfied image file and scans through the data to check if it is a QR code.
    If it is found and successfully decoded it will display the message. If unsuccessful it will print
    an error message saying the image was not a QR code or was too degraded.
    
    Note: Code was majority adapted from the qrcode website.
    
    Arguments:
    ----------
    
    image_file  - The image file to be scanned [MUST be a valid image file]
    
    Returns:
    --------
    
    message     - Either "Success (MESSAGE)" or "Fail", where message is the message encoded.
    
    Usage: 
    ------
    
    decode("code.png") - Checks the image file "code.png" for a QR code and displays the results.
    
    """
    
    # Set message
    message = ""
    
    # Create a zbar image reader
    scanner = zbar.ImageScanner()
    
    # Set the reader configuration to default
    scanner.parse_config('enable')
        
    # Read the image file and convert it into greyscale data readable by zbar
    try:
        pil = Image.open(image_file).convert('L')
    except:
        # Image file is not an image
        print "Sorry, the file provided was not an image."
        raise TypeError
        
    width, height = pil.size # Extract image size
    raw = pil.tostring() # Convert image to a string of data
    
    # Put the image data in a container with the size and data together
    image = zbar.Image(width, height, 'Y800', raw)
    
    # Use zbar to scan the data for a QR code
    scanner.scan(image)
    
    # Scan through results
    for symbol in image:      
        
        # Check image is actually a QR code
        if str(symbol.type) == "QRCODE":
            # Set message to success and include the encoded message
            message = "Success ({0})".format(symbol.data)
            # Exit
            return message
    
    # If results do not contain a zbar symbol (unsuccessful read)        
    else:
        # Set message to fail
        message = "Fail"     
        # Exit
        return message

    
#################
# End Functions #
#################

##############
# End Module #
##############