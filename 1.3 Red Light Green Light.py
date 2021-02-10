#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Applications of KNN: Red Light Green Light
# Have you ever played the game "Red Light Green Light"? Here are the rules: a referee calls out "red light" or "green light" to players who are trying to race to a finish line. If the referee calls out red light, players must stop and freeze in their places. If the referee calls "green light", players race to the finish line. Whoever arrives first wins!
# 
# In this lesson, you will teach Zumi that green means go and red means stop. This is pretty important for self-driving cars to know since cars stop (and go!) at traffic lights every day.
# 
# 
# ### Step 1: Import Libraries
# In this lesson, we are using the Zumi library for drive commands, the Camera library for training, the Screen library for printing text and emotions, and threading for running multiple processes at once.
# 

# In[ ]:


from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from threading import Thread
from zumi.util.color_classifier import ColorClassifier

zumi = Zumi()
camera = Camera()
screen = Screen()


# ### Step 2: Gather data
# 
# Run the code below and train Zumi with green and red color cards. Name your demo ```red_green``` so you can find it again easily and use the following labels and key commands:
# 
# * Label: ```green```   Key Command: ```g```
# * Label: ```red```     Key Command: ```r```
# 

# In[ ]:


camera.start_camera()
try:
    knn = ColorClassifier()
    train = knn.set_values()
    
    if train:
        print("Start gathering data. If you want to stop, press q")
        cnt = int(input("Type the amount of the pictures that you want to take at once : "))
        while True:
            knn.add_datas(camera, cnt)
            if knn.check_enough_datas(balance=True):
                break

        knn.save_data_set()
        knn.get_accuracy()
finally:
    camera.close()


# ### Step 3: Test the model
# Before you start adding drive commands, test the model to check that your data has been trained correctly. Test it with some other objects too to see how reliable it is. If you need to, retrain the data under a different model name.

# In[ ]:


try:
    print("Start predicting, press enter to predict!")
    camera.start_camera()
    knn.fit("hsv")
    while True:
        if input("press enter (or q to exit) : ") == 'q':
            break
        image = camera.capture()
        predict = knn.predict(image)
        print(predict)
finally:
    camera.close()


# 
# ### Step 4: Program logic
# Once you’re finished testing your model, you can write out the logic with print statements.
# 
# When you call ```knn.predict(image)```, it returns its prediction with a label. For example, if you train the model with labels named ```blue``` and ```yellow```, some code might look like this:
# 
# ```
# while True:
#     if input("Press "enter" to predict or "q" to exit.") == "q":
#         break
#     image = camera.capture()
#     predict = knn.predict(image)
#     if predict == "blue":
#         zumi.forward()
#     if predict == "yellow":
#         zumi.reverse()
# camera.close()
# ```
# The labels are in quotes because they are **string** data types. Strings are strings of characters, letters, or numbers that are treated as text. These labels must match your data labels EXACTLY. If you accidentally mistyped "blu" for your label but wrote your code to check if predict is equal to "blue", this code would never run.
# 
# Try writing the Red Light Green Light program with print statements. If the code says "CHANGE ME", make sure to make those changes to the correct labels for this project.
# 

# In[ ]:


try:
    print("Start predicting, press enter to predict!")
    camera.start_camera()
    knn.fit("hsv")
    
    while True:
        if input("press enter (or q to exit) : ") == 'q':
            break
        image = camera.capture()
        predict = knn.predict(image)
        if predict == "CHANGE ME":
            # Add a print statement here for driving forward
        if predict == "CHANGE ME":
            # Add a print statement here for stop

finally:
    camera.close()


# ### Step 5: Threading and go_straight()
# Once you have tested your program logic with print statements, you need to add drive commands. Your first thought might be to write out your program logic like this:
# 
# ```
# if predict == "green":
#         zumi.forward()
#     if predict == "red":
#         zumi.stop()
# ```
# 
# ```Forward()``` drives Zumi for a number of seconds that you specify and then stops, but you will want Zumi to stop driving *only* when she sees a red card. In this case, you need to use threading. This allows you to run multiple processes at the same time. Think of it like weaving two separate functions together so that they appear to be running simultaneously.
# 
# When you start a thread, it starts running in the background and lets the rest of the program continue running. You can use a **boolean**, or a true/false statement, to start or stop Zumi. The variable that you make for your boolean needs to be **global** so it can be used throughout the entire program instead of just one section. We named our variable ```is_green``` and we set it to ```false``` so that Zumi begins the program at a stop. We also defined our function ```continue_straight()```, which needs to be running in the background while ```is_green``` is ```true```. Once Zumi sees red, ```is_green``` becomes false, which will break the while loop (you can see that at “while is_green”) and cause Zumi to stop.
# 
# The cell below defines this function. Don't worry, Zumi won't start driving just yet.
# 
# 

# In[ ]:


global is_green
is_green = False

def continue_straight():
    while is_green:
        zumi.go_straight(20, 0)
    zumi.stop(0)


# Now you can weave these codes together with threading.  If Zumi sees green, you need to set the boolean to ```True``` and begin the thread. If Zumi sees red, ```is_green``` is now ```False```.
# 
# ```
#   if predict == "green":
#         is_green = True
#         drive_thread = Thread(target=continue_straight)
#         drive_thread.start()
#     if predict == "red":
#         is_green = False
#         zumi.stop()
# ```
# 
# 
# Here is all of the code put together. Try it out!
# ### Step 6: Final code

# In[ ]:


try:
    print("Start predicting, press enter to predict!")
    camera.start_camera()
    knn.fit("hsv")
    
    while True:
        if input("press enter (or q to exit) : ") == 'q':
            break
        image = camera.capture()
        predict = knn.predict(image)
        if predict == "green":
            is_green = True
            drive_thread = Thread(target=continue_straight)
            drive_thread.start()
        if predict == "red":
            is_green = False
            zumi.stop()
finally:
    is_green = False
    zumi.stop()
    camera.close()


# ## Challenge
# If you want, add more colors and have Zumi do different drive commands for each one!
