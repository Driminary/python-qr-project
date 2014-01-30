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
#    29/01/2014   #
###################

##########################
# Python QR Code Project #
# ---------------------- #
#      Main Program      #
##########################

# Import modules
import mod_encode_decode as qr_ed # My encoding-decoding module
import mod_imgtools as qr_imgtools # My image processing module

# Run encoding module
qr_ed.encode("Random Message","code")

# Run decoding module
qr_ed.decode("code.png")

# Run compare function from imgtools
print qr_imgtools.compare("calibration_purewhite.png","calibration_25percent.png")