# -*- coding: utf-8 -*-
# @author: Thomas Anderson
 
###################
#   run_expt.py   #
###################
# Thomas Anderson #
###################
#    29/01/2014   #
###################
#  Last updated:  #
#    11/03/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#      Main Program      #
##########################

"""
===========
Version 1.0
===========
 Released:
11/03/2014
===========

=========================================================================================================
Requires: random, string [Included in python installation], mod_imgtools and mod_encode_decode [Supplied]
=========================================================================================================

A program used to encode, degrade and then test qr codes to see if each error setting can read the images
produced using the specified blur radius and image size.

In this directory are the two modules required for the program to run, mod_imgtools and mod_encode_decode.
Also in the directory are two folders named 'images' and 'data' used to keep the structure of the files
in an ordered manner. 

- images/calibration_purewhite.png  = A 100 x 100 px pure white image
- images/calibration_25percent.png  = The file above with a 50 x 50 px black square in the top left
                                      covering 25% of the image.
- mod_encode_decode.py              = Thomas Anderson's encoding and decoding module.
- mod_imgtools.py                   = Thomas Anderson's image processing module.

For usage of each function, please refer to the DOCSTRING. There are a few user configurable variables
which can be altered and set to different values in order to produce different output files.

Changing the 'blur' variable will alter the amount that each set of pixels is gaussian blurred by to
produce the image to be tested.
Changing the 'maxsize' variable will alter the maximum image size that will be created for testing.

Each image is degraded and tested to see if it can be decoded and then the program will produce a text 
file in the data folder indicating the results of the test.

This program may be ran standalone, but the required modules must be included in a file.

Remeber that due to the licensing this file is released under (MIT License), all usage must include
credit to the original owner (myself) and so you must include the first line if you import or it will
be an infringement of copyright.

Source files can be found on https://github.com/Driminary/python-qr-project

"""

# Import modules
import mod_encode_decode as qr_ed   # My encoding-decoding module
import mod_imgtools as qr_imgtools  # My image processing module
import random, string

############################
# User Configuration Start #
############################

# Set blur radius [Set this around 5-25 for best results]
blur = 5

# Set max image size [To stop massive resource usage, keep this below 15]
maxsize = 10

##########################
# User Configuration End #
##########################

# Check blur is positive integer
assert int(blur) > 1 , "The specified blur was not a valid number"

# Check maxsize is positive integer
assert int(maxsize) > 1 , "The specified maximum size was not a valid number"

# Set message as a randomly generating string of letters and numbers 32 characters long
message = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

# Open file to write output to
f = open("./data/data_blur_%s_output.txt" % blur, "w")

# Print the message - write to file
print >>f , "\n================\nThe message encoded this run is: ", message, "\n================\nBlur Radius = %s\n================\nMax Size = %s\n================" % (blur,maxsize)


# Initialise counter
i = 1

# Do a set of tests for all error settings
while (i <= 4):
    
    # Print image size (run number) - write to file
    print >>f , "\n================\nError Setting = %s\n================\n" % (i) 
    
    # Initialise counter
    j = 1
    
    # Repeat for the sizes 1 -> max size
    while (j <= maxsize):
        
        # Run encoding function from encode_decode for each error redundancy
        qr_ed.encode(message,"code_{0}".format(j),j,i) 

        # Run addblur function from imgtools
        qr_imgtools.addblur(blur,"./images/code_{0}.png".format(j))

        # Run compare function from imgtools - write to file
        print >>f , "The reading of image size ", j, "was a ", qr_ed.decode("./images/code_{0}_blurred.png".format(j)) 
        
        # Increase counter
        j += 1
    
    # Increase counter
    i += 1

# Print a success message, if the program failed at any point, the error handling in the code should take care of it.
print "Complete, wrote output to ", f.name

# Close the file
f.close()