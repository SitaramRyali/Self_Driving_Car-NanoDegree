**Finding Lane Lines on the Road**

The project is baout finding the lane lines on the road with basic line detecting techniques.

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Apply these pipeline on images
* Apply these pipeline on Videos which are series of images.


Lane finding Pipeline
---
My pipeline consisted of 5 steps. 
**Step 1:**  Read in the image into the memory and then covert in into grayscale.
Image size here is 540x960 as a grayscale channeled image

!["Grayscale"]: (../master/test_images/solidYellowLeft_gray.jpg)

---

**Step 2:**  Blur the image and then Apply Canny edge detcetion.
The parameters used for generalization here are: low_thresold :100 and High_thresold:200

!["Canny"]: (../master/test_images/solidYellowLeft_canny.jpg)

---
**Step 3:**  Use the image output from canny edge detector and make the region of intereset.
The method followed here is based on the truth that our road line lie under camera visible low boundary.
For this I have used the corners of x-plane when y=540.
Then I have arranged a polygon to detect the lower bound of camera view.

---
**Step 4:**  Apply Hough line transform to detect the line patterens in the ROI image.
The parameters used in the Hough transform are as below:
rho =1, and theta = pi/180 whihc are generailzed values.
Thresold = 50 ; min_line_length = 40; max_line_gap = 400
These are the uniques parameters space for this task ,where I have suppressed the need for intrapolation or averaging of lines.
Above parameters helped me to get the same sloped lines till the point of intereset.

![Lane_lines Detected]: (../master/test_images/solidYellowLeft_out.jpg)
	
---


### 2. Potential shortcomings with the current pipeline


One potential shortcoming would be detecting the curved lines.

Another shortcoming could be noisy images where the lines are not exactly lines, like arrow signs on road.
Another one could be lines like zebra crossings, where current detecto fails to seperate them when in near of sight of camera.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to use advanced curve detecting algorithms for the better detcetion

Another potential improvement could be to seperate the lines like zebra crossings from the pipeline.
The one ore best possible way is to fuse the current development alog with the CNN netwrok, 
where it can detect only roadlines , as we can supply some infomation to system at front.
