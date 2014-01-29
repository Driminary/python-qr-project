# -*- coding: utf-8 -*-
# @author: Thomas Anderson
 
########################
# mod_encode_decode.py #
########################
# Thomas Anderson #
###################
#    29/01/2014   #
###################
#  Last updated:  #
#    29/01/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#   Encoding/Decoding    #
#        Module          #
##########################

"""

A module to generate a QR code from a user inputted string, as well as decode a given image file to determine
if it is a QR code and what the message is.

Requires: qrcode, zbar, Python Image Library (PIL)

In this directory is a .zip file containing the win32 binaries for PIL and zbar and the source files for qrcode.

"""

################
# Begin Module #
################

# If module is being run on its own, not imported as a module, exit gracefully.
if __name__ == '__main__':
    print "Please import the module rather than run it standalone."
    raise RuntimeError
    
# Import required modules
import qrcode
import zbar
import Image

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
    
    # Print a success message
    print "File outputted to %s.png" % image_name
    
    return
    
#    # create a reader
#    scanner = zbar.ImageScanner()
#    
#    # configure the reader
#    scanner.parse_config('enable')
#    
#    # obtain image data
#    pil = Image.open("code.png").convert('L')
#    width, height = pil.size
#    raw = pil.tostring()
#    
#    # wrap image data
#    image = zbar.Image(width, height, 'Y800', raw)
#    
#    # scan the image for barcodes
#    scanner.scan(image)
#    
#    # extract results
#    for symbol in image:
#        # do something useful with results
#        print 'Image was a ', symbol.type, ', and contained the following message: \n', symbol.data
#    
#    # clean up
#    del(image)
    
#################
# End Functions #
#################

##############
# End Module #
##############