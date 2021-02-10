#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Demo: Object Tracking
# 
# **OpenCV** (Open Computer Vision) is an open-source library primarily dealing with real-time computer vision.
# 
# Computer vision is exactly what it sounds like: it’s the field dedicated to helping computers see. With computer vision, machines can extract important information from images. This is really easy for humans but more challenging for computers. A lot of progress has been made in the past decade --- think of how your phone’s camera can recognize faces now! Computer vision is used in everything from robot navigation to medical image analysis.
# 
# This lesson is a demo on how computer vision and image processing can be used to track objects.
# 
# ### Import libraries

# In[1]:


from zumi.util.camera import Camera
import cv2
import numpy as np
import time
import IPython.display
import PIL.Image


# ### ROI (Region of Interest)
# 
# Using the ROI method is a simple way to track objects. We choose an object to track by selecting an area of pixels. If the area of pixels moves from one frame to the next, the algorithm will track this change. Below is the code to set up the functions you will need to do object tracking. Run the code to set up all of the functions for object tracking.

# In[ ]:


class MeanShift:
    def __init__(self):
        self.hsv_lower = None
        self.hsv_upper = None
        self.H = 0
        self.W = 0
        self.X = 0
        self.Y = 0
        self.LEN = 0
        self.L = 0
        self.MIN_LEN = 0
        self.DENSE = 0
        self.term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    def get_track_window(self):
        return self.X, self.Y, self.LEN, self.LEN
    
    def set_first_ROI(self, camera):
        image = camera.capture()
        self.__set_track_window(image)
        x,y,w,h = self.get_track_window()
        
        k = ''
        while k != 'ok':
            image = camera.capture()
            image = cv2.rectangle(image, (x,y), (x+w,y+h), 255, 2)            
            IPython.display.display(PIL.Image.fromarray(image))
            k = input("press enter to take new picture \n If it's good to go, type 'ok'")
        
        roi = image[y:y+h, x:x+w]        
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        self.set_hsv_range(roi)
        roi = cv2.inRange(roi, np.array(self.hsv_lower), np.array(self.hsv_upper))
        self.DENSE = self.get_dense(roi)
        
    def find_new_location(self, image, show=True):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image= self.colorShift(hsv)
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        
        x,y,w,h = self.get_track_window()
        image = cv2.rectangle(image, (x+self.L,y+self.L), (x+w+self.L,y+h+self.L), 255,2)
                
        if show:
            IPython.display.display(PIL.Image.fromarray(image))
    
    def colorShift(self, image):
        L = self.L
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.copyMakeBorder(image, L, L, L, L, cv2.BORDER_CONSTANT, None, (0,0,0))
        image = cv2.inRange(image, np.array(self.hsv_lower), np.array(self.hsv_upper))

        X = [0, -L, L, 0, -L, L, 0, -L, L]
        Y = [0, 0, 0, -L, -L, -L, L, L, L]
        
        MAX_D = 0
        MAX_X = -1
        MAX_Y = -1
        for y in range(9):
            for x in range(9):
                dense = self.get_dense(image[(self.Y+Y[y]+L):(self.Y+self.LEN+Y[y]+L), (self.X+X[x]+L):(self.X+self.LEN+X[x]+L)]) 
                if dense > MAX_D :
                    MAX_D = dense
                    MAX_X = X[x]
                    MAX_Y = Y[y]
        self.X = self.X + MAX_X
        self.Y = self.Y + MAX_Y
        self.DENSE = MAX_D

        s_dense=0
        b_dense=0
        
        if self.LEN > self.MIN_LEN:
            s_dense = self.get_dense(image[(self.Y+2+L):(self.Y+self.LEN-2+L), (self.X+2+L):(self.X+self.LEN-2+L)])
        if self.LEN < self.H - 4 :
            b_dense = self.get_dense(image[(self.Y-2+L):(self.Y+self.LEN+2+L), (self.X-2+L):(self.X+self.LEN+2+L)])
        
        if b_dense > self.DENSE or b_dense > 0.8:
            self.X = self.X-2
            self.Y = self.Y-2
            self.LEN = self.LEN+4
            self.DENSE = b_dense
        elif s_dense > self.DENSE + 0.01:
            self.X = self.X+2
            self.Y = self.Y+2
            self.LEN = self.LEN-4
            self.DENSE = s_dense
            
        return image
        
    def set_hsv_range(self, image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        h, s, v = cv2.split(hsv_image)
        min_h, max_h = self.get_range(h)
        min_s, max_s = self.get_range(s)
        min_v, max_v = self.get_range(v)
        print("min/max of hsv values")
        print(min_h, min_s, min_v)
        print(max_h, max_s, max_v)
        input("press any key for start")
        
        self.hsv_lower = [min_h-10, min_s-30, min_v-20]
        self.hsv_upper = [max_h+10, max_s+30, 255]
        
    def get_range(self, data):
        data = np.ravel(data)
        data.sort()
        return data[0], data[-1]
      
    def get_dense(self, image):
        h, w = image.shape 
        if (h * w)==0:
            return 0
        dense =  ((h*w) - np.count_nonzero(image==0))/ (h * w)
        return dense
        
    def __set_track_window(self, image):
        self.H, self.W, d = image.shape
        self.X = int(self.W/2-self.H/6)
        self.Y = int(self.H/2-self.H/6)
        self.LEN = int(self.H/3)
        self.L = int(self.LEN/3)
        self.MIN_LEN = int(self.LEN/2)


# ### Track a color card
# Choose one of your color cards and set it in front of Zumi. Continue pressing ```enter``` until you are sure that your object is within the red bounding box. Once you have a good image, type ```ok``` to select it. The program will start tracking your object! What other objects can you track?
# 

# In[ ]:


mean = MeanShift()
camera = Camera()
time.sleep(1)

try:
    camera.start_camera()
    mean.set_first_ROI(camera) 
    first_window = mean.get_track_window()
    while True:
        image = camera.capture()
        mean.find_new_location(image)
        IPython.display.clear_output(wait=True) 
finally:
    camera.close()


# We have lots of other lessons in progress that will teach you how to use this information to do cool robotics projects! Feel free to create your own Jupyter Notebooks and write code that combines everything you have learned so far. Stay tuned for more content!
