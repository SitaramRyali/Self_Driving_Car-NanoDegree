#analysing the resizing functinality of Cv2.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def resize_image(image):
    resized_img = cv2.resize(image,(1000,500))
    return resized_img
img_1 = mpimg.imread('exit-ramp.jpg')
resized_img_1 = resize_image(img_1)


fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
plt.imshow(resized_img_1)

img_2 = mpimg.imread('road_lanes.jpg')
resized_img_2 = resize_image(img_2)

a = fig.add_subplot(1, 2, 2)
plt.imshow(resized_img_2)

plt.show()