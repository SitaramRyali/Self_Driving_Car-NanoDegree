import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


# Read in and grayscale the image
image = cv2.imread('road_lanes.jpg')
random_fun = np.ones_like(image)
im_shape = image.shape
#np.random.seed(10)
#temp = np.random.randint(im_shape[0],im_shape[1])
random_fun[:,:,0] = np.random.randn(im_shape[0],im_shape[1])
random_fun[:,:,1] = np.random.randn(im_shape[0],im_shape[1])
random_fun[:,:,2] = np.random.randn(im_shape[0],im_shape[1])
plt.imshow(random_fun)
plt.show()