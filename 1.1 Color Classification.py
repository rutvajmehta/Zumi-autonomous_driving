#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Lesson 1: KNN Color Classifier
# 
# You can see colors and differentiate between them, but did you know computers can do this too? In this lesson, you will learn how to use a special **algorithm** to teach Zumi different colors. This is a very basic example of machine learning, which can be summarized in three steps:
# 
# * Gathering data
# * Generating a model
# * Making predictions
# 
# Up until now, Zumi has only known about black and white. You will use Zumi's camera to take many pictures of your favorite colors, then run code that will use the color information to label each color. In the final step, you will be able to test your model and write code for Zumi to react to each one differently! For now, let's teach Zumi about colors.
# 
# 

# ### Step 1: Import libraries and create objects
# This cell imports all of Zumi’s necessary features, like the camera. If you don’t run this cell, the rest of your program won’t work!

# In[ ]:


from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from zumi.util.color_classifier import ColorClassifier
import time

camera = Camera()
screen = Screen()
zumi = Zumi()


# ### Step 2: Set & Collect Training Data
# You are going to train Zumi to distinguish between two different colors. Pick your two favorite colors from the color cards and have them ready for training.
# 
# When you run the code, it will ask you to enter the following:
# 
# * **Demo Name:** The name of this activity. Keep it short so you remember which program you are working on. For example: ```RedBlue```
# 
# * **Number of labels:** This is the number of colors you want to train Zumi to recognize. For example, if you have red and blue, you would input ```2```.
# 
# * **Label Names and Key commands:** For each color, make sure you type the name of your color and the associated key that will tell Zumi which color it is. For example, the label name for red might be red and the keyboard command can be the letter ```r``` . The only key you cannot use as a command is the letter ```q``` because that key quits the program. After each color, verify that your labels and commands are correct by pressing ```enter```.Make sure you remember your key commands because you will need them later when you collect the training data.
# 
# 
# then,
# 
# * Gather the cards that are the colors of the labels you chose. 
# * The program will ask you how many pictures you will take at a time. For this demo, input ```10```. You will need a minimum of 50 pictures for your project to work.
# * Place each one about 5in away from Zumi camera and press the corresponding key command for that color on your keyboard. 
# * Check the label on the terminal and press enter to confirm. If you want to delete any data, follow the onscreen instructions. 
# * Try taking pictures in different lighting and from different angles!
# 
# When you are done, press the letter ```q``` to quit.
# 
# 
# **Note**: If you ever have errors with the camera, close the notebook and reopen it. A rule of thumb is to keep the ```try``` and ```finally``` statements in your code. You will learn later how this works.

# In[ ]:


camera.start_camera()

try:
    knn = ColorClassifier()
    train = knn.set_values()

    if train:
        print("Start gathering data. If you want to stop, press `q`")
        cnt = int(input("Enter the amount of the pictures that you want to take at once : "))
        while True:
            knn.add_datas(camera, cnt)
            if knn.check_enough_datas(balance=True):
                break

        knn.save_data_set()
        knn.get_accuracy()
finally:
    camera.close()


# ### Step 3: Predict
# Run the following code to predict the values. Gather various objects and place them in front of the camera. Press the ```enter``` key to have Zumi guess the color. Does Zumi get them right? When you are done, press ```q``` to quit.

# In[ ]:


try:
    print("Start predicting, press enter to predict!")
    camera.start_camera()
    knn.fit("hsv")
    while True:
        if input("Press `enter` to predict or `q` to exit): ") == 'q':
            break
        image = camera.capture()
        predict = knn.predict(image)
        print(predict)
        screen.draw_text(predict)
finally:
    camera.close()


# # How do computers see and interpret colors?
# 
# ## What is an image?
# An image is made up of an array of small dots called The **pixels** (short for picture element). A pixel can be a single color or a combination of colors, and each of those colors is represented by a series of three numbers that tell you exactly how much red, green, and blue are in it. This is called the **RGB** value, which stands for red, green, and blue. For example, a beautiful shade of turquoise might look something like (27, 209, 197) since there isn’t a lot of red, but there is a lot of green and blue. Because each value of RGB can be between 0 and 255, there are 256 values to choose from for each color. That results in 256^3, or 16,777,216, different color combinations!
# 
# 
# ## What is a matrix?
# Since each pixel can be represented by numbers, a picture is a grid of numbers. This is where humans and computers start to see images a little differently. Humans see colors and shapes that we recognize as different objects, but computers only see this grid of numbers, also called **matrices**. Each number represents the RGB value of each pixel. They look a little like this:
# 
# <img src="../Data/images/matriceszumi.png" width=500>
# 
# ## Using HSV instead of RGB
# 
# In this activity, you trained Zumi to recognize different colors. You used the camera to collect training data pictures, and then ran a special classifier to classify the colors. The computer processed all the number values of the image matrix to label each color, and then used those values to guess the colors.
# 
# You learned about the RGB colorspace, but this program converted each RGB image to the **HSV** colorspace. HSV stands for hue, saturation, and value.
# 
# 
# * **Hue** normally ranges from 0-360 and represents the color (in this application however, it ranges from 0-180)
# * **Saturation** is the color's intensity
# * **Value** is how light or dark the color is
# 
# In computer vision applications, it is better to use the HSV colorspace since it separates values for colors and intensity. This is important because shadows, reflections, and other factors may cause certain colors look very different. The HSV colorspace takes this into account for more accurate results.
# 
# 
# <img src="../Data/images/HSVdiagram.png" alt="hsv" width="400"/>
# 
# 

# 
# 
# 
# ## Challenge
# Use all of the colors in the box and then try testing out the predictions on different items around your environment. Run cells for step #1 and step #2 respectively. Make sure you name your demos some different every time!
