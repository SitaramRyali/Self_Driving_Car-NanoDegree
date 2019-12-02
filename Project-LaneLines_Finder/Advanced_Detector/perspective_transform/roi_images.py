#analysing the resizing functinality of Cv2.
import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from apply_sobel import abs_sobel_thresh

images =  glob.glob('test_images/*.jpg')
im_base = cv2.imread(images[0])
imshape = im_base.shape

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image



#define perspective transormation function
def warp(img,src,dst):
    #define calibration box in source and destination
    img_size = (img.shape[1], img.shape[0])

    
    #compute the perspective image transformation mapping
    M = cv2.getPerspectiveTransform(src, dst)
    
    #could compute the inverse also by swapping the input parameters
    Minv = cv2.getPerspectiveTransform(dst,src)
    
    #create warped image - uses the linear interpolation
    warped = cv2.warpPerspective(img, M,img_size,flags = cv2.INTER_LINEAR )
    #create unwarped image - uses the linear interpolation
    unwarped = cv2.warpPerspective(img, Minv,img_size,flags = cv2.INTER_LINEAR )
    
    return warped,unwarped

y_bottom_idx = imshape[0]-50
y_top_idx = 500
x_left_bottom= 200
x_right_bottom= 1200
x_left_top = 500
x_right_top = 900

#four co-ordinates
src = np.float32([[x_right_top, y_top_idx],
                  [x_right_bottom,y_bottom_idx],
                  [x_left_bottom,y_bottom_idx],
                  [x_left_top, y_top_idx]])
dst = np.float32([[x_right_bottom,0],
                  [x_right_bottom,y_bottom_idx],
                  [x_left_bottom,y_bottom_idx],
                  [x_left_bottom,0]])

vertices = np.array([[(x_left_bottom,y_bottom_idx),(x_left_top, y_top_idx), (x_right_top, y_top_idx), (x_right_bottom,y_bottom_idx)]], dtype=np.int32)
for each in images:
    im = cv2.imread(each)
    mask_img = region_of_interest(im,vertices)
    warped_im,_ = warp(mask_img,src,dst)
    im_name = each[-5:]
    cv2.imshow('org_im',im)
    cv2.waitKey(1)
    cv2.imshow('roi_image',warped_im)
    cv2.waitKey(0)
    #mpimg.imsave(im_name,warped_im)
    #warped_im = cv2.cvtColor(warped_im, cv2.COLOR_BGR2RGB)
    cv2.imwrite(im_name,warped_im)  
cv2.destroyAllWindows()