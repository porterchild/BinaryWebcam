import numpy as np
import sys
from SimpleCV import Camera

# Initialize the camera
cam = Camera()

#image dimensions - THIS COULD CHANGE BASED ON THE CAMERA
width = 480
height = 640

#this is what goes on the screen for a dark or light pixel
dark = 1
light = 0

#make it a 1/4 scale of the actual picture
binary_representation = [[0 for x in xrange(0, width/4)]for y in xrange(height/4)]

# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()

    #PRINT THIS IF YOU ARE GETTING 'OUT OF RANGE' ERRORS AND NEED TO CHECK YOUR IMAGE
    #DIMENTIONS:
    #print img

    # Make image black and white
    img = img.binarize()

    #loop to pixels and transcribe image to binary_representation (every 4 pixels to save time)
    for i in xrange(0, height - 1, 4):
        for j in xrange(0, width - 1, 4):
            if img[i, j][0] == 0:
                binary_representation[i/4][j/4] = light
            else:
                binary_representation[i/4][j/4] = dark
    #print binary_representation
    for i in xrange(0, width/4):
        for j in xrange(0, height/4):
            sys.stdout.write(str(binary_representation[j][i]))
        sys.stdout.write('\n')

    # Show the image
    #img.show()
