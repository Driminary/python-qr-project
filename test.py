# -*- coding: utf-8 -*-
 
###################
#   py12tja.py    #
###################
# Thomas Anderson #
###################
#    15/11/2013   #
###################
#  Last updated:  #
#    17/11/2013   #
###################

##########################
# Python QR Code Project #
##########################

import qrcode
import zbar
import Image

# get user input
inp = raw_input("Please type what you would like encoding: ")

# create qr code from user input
f = qrcode.make(str(inp))

# save image
f.save("code.png")

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open("code.png").convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    print 'Image was a ', symbol.type, ', and contained the following message: \n', symbol.data

# clean up
del(image)

###############
# End Program #
###############