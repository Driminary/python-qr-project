# -*- coding: utf-8 -*-
# @author: Thomas Anderson
 
###################
#     test.py     #
###################
# Thomas Anderson #
###################
#    29/01/2014   #
###################
#  Last updated:  #
#    12/02/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#      Main Program      #
##########################

# Import modules
import mod_encode_decode as qr_ed   # My encoding-decoding module
import mod_imgtools as qr_imgtools  # My image processing module
import random, string

# Initialise counter
i = 1

# Set blur radius
blur = 5

# Set message as a randomly generating string of letters and numbers 32 characters long
message = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

# Print the messag
print "The message encoded this run is: ", message

# Do a set of tests on image of size 1 -> the value below
while (i <= 10):
    
    # Print image size (run number)
    print "\n================\nImage Size = %s\n================\nBlur Radius = %s\n================" % (i,blur) 
    
    # Initialise counter
    j = 1
    
    # Repeat for all error settings
    while (j <= 4):
        
        # Run encoding function from encode_decode for each error redundancy
        qr_ed.encode(message,"code_{0}".format(j),i,j) 

        # Run addblur function from imgtools
        qr_imgtools.addblur(blur,"code_{0}.png".format(j))

        # Run compare function from imgtools
        print "\nThe images with error setting ", j, "are ", qr_imgtools.compare("code_{0}.png".format(j),"code_{0}_blurred.png".format(j)), "% different.\nReading blurred image...", qr_ed.decode("code_{0}_blurred.png".format(j))

        # Increase counter
        j += 1
    
    # Increase counter
    i += 1