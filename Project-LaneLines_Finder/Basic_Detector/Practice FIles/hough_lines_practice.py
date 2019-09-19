#hough line practice.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = mpimg.imread('ex_white.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

edges = cv2.Canny(gray, 75, 150)
# Define the Hough transform parameters
# Make a blank image the same size as our image to draw on
rho = 1 # distance resolution in pixels of the Hough grid
theta = np.pi/180 # angular resolution in radians of the Hough grid
threshold = 15     # minimum number of votes (intersections in Hough grid cell)
min_line_length = 20 #minimum number of pixels making up a line
max_line_gap = 220    # maximum gap in pixels between connectable line segments
#line_image = np.copy(image)*0 # creating a blank to draw lines on


# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on a blank image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
plt.imshow(img)
plt.show()