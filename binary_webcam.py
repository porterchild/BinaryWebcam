import numpy as np
import sys
from SimpleCV import Camera
# Initialize the camera
cam = Camera()
# Loop to continuously get images
width = 480
height = 640
dark = 1
light = 0

binary_representation = [[0 for x in xrange(0, width/4)]for y in xrange(height/4)]
while True:
    # Get Image from camera
    img = cam.getImage()
    # Make image black and white
    img = img.binarize()
    for i in xrange(0, height - 1, 4):
        for j in xrange(0, width - 1, 4):
            if img[i, j][0] == 0:
                binary_representation[i/4][j/4] = light
            else:
                binary_representation[i/4][j/4] = dark
    for i in xrange(0, width/4):
        for j in xrange(0, height/4):
            sys.stdout.write(str(binary_representation[j][i]))
        sys.stdout.write('\n')

    # Show the image
    #img.show()
