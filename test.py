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

# image to import
f = qrcode.make("Hello")

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open(f.convert('L'))
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del(image)

###############
# End Program #
###############