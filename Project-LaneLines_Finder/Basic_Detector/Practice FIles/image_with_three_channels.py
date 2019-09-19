#image_with_three_channels
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
org_img = mpimg.imread('road_lanes.jpg')

fig = plt.figure()
a = fig.add_subplot(1, 4, 1)
imgplot = plt.imshow(org_img)
a.set_title('Original Image')
channel_data = ['red','green','blue']


for i in range(3):
    a = fig.add_subplot(1, 4, i+2)
    imgplot = plt.imshow(org_img[:,:,i])
    a.set_title('{} channel image'.format(channel_data[i]))
plt.show()