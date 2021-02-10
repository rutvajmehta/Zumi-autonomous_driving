#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # Robot Emotions
# 
# Zumi has a personality! In this lesson, you will learn how Zumi detects human emotions as well as how to program Zumi’s personality. You will also learn about sound, how it’s measured, and how it corresponds with emotion.  Finally, you will train your Zumi to recognize and react to her favorite color.
# 
# 
# 
# ## How do we detect emotion?
# Take a look at the images below and see if you can identify each of the emotions. 
# 
# ![emotions](../Data/images/emotions.png)
# 
# How did you determine which emotion was which? There are many features that can be indicators, like eyes, mouth, eyebrows, and maybe gestures. How do we translate human emotions to a robot?
# 
# If you have seen the movie *Cars*, you may know that each of the cars has a personality. How was each car able to express emotions? Was it through movements? Sounds? Eyes?
# 
# 
# ### Import libraries
# To use personality functions, we need to import Zumi, Screen, and Personality.
# 

# In[ ]:


from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.personality import Personality
import time

zumi = Zumi()
screen = Screen()
personality = Personality(zumi, screen)


# ###  Calling personality functions
# Here are some functions you can call:
# 
# * happy()
#      
# * celebrate()
#        
# * angry()
#        
# * look_around()
# 
# * look_around_open()
#        
# * disoriented_left()
#        
# * disoriented_right()
# 
# * awake()
# 
# For example, 
# ```personality.happy()``` will make Zumi wiggle and make a sound!
#             
# In the cell below,try testing out some of the pesonality functions to see what they do.

# In[ ]:


# Test Personality code here!


# ## Sounds
# 
# Zumi can play sounds to match her emotions! Sound can be measured in frequency and amplitude. Frequency is the number of pulses or vibrations per second, and is measured in hertz. The higher the frequency, the higher the pitch of the sound is. Amplitude is how loud or strong the sound is and is measured in decibels. The higher the amplitude, the louder the sound is. 
# 
#  Video: [Sound: Wavelength, Frequency, and Amplitude](https://www.youtube.com/watch?v=TsQL-sXZOLc)
# 
# What does each emotion sounds like? Is happy a low or high frequency? Is angry a low or high amplitude? How does this apply to Zumi?
# 
# You can use ```play_note()``` to play various notes. The first parameter is the note you want to play (anywhere from C2 to B6). The second parameter is optional and denotes the amount of time you want the note to play in milliseconds. The default value is set to 500ms but you can change that by adding a second parameter like this: ```play_note(Note.GS3, 400)```. This plays the note G Sharp below middle C for 400ms.
# 

# In[ ]:


from zumi.protocol import Note 
zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)
zumi.play_note(Note.F4)
zumi.play_note(Note.G4)
zumi.play_note(Note.A4)
zumi.play_note(Note.B4)
zumi.play_note(Note.C5)


# Code your own sounds for happy, sad, angry, or excited. Try out different melodies until you find your favorites.

# In[ ]:


# Make your melodies here 🎵 


# ## Screen
# 
# Zumi personality also uses the **OLED** (organic LED) screen to display emotions.
# There are many different "eyes" Zumi has:
# ```
# * close_eyes()
# * sleepy_eyes()
# * sleepy_left()
# * sleepy_right()
# * blink()
# * look_around_open()
# * sleeping()
# * look_around()       
# * glimmer()
# * sad()
# * happy()
# * hello()
# * angry()
# ```
# 
# To use the screen, call the screen class with a function of your choice. Try this:
#       

# In[ ]:


screen.sad()


# ### Draw Text
# 
# Aside from drawing Zumi eyes, you can also have Zumi write messages on the screen! Use the ```draw_text()``` function to write a message like this:

# In[ ]:


screen.draw_text("hello!")


# If you want to automatically center the text on the screen, call this function instead:

# In[ ]:


screen.draw_text_center("hello!")


# If you want to to write text with numbers, you need to make sure everything is of the ```String``` data type.

# In[ ]:


number = 10
screen.draw_text("ten " + str(number)) # the str() functions turns the number into a string


# You can even make Zumi display the time for you!

# In[ ]:


for i in range(0,50):
    screen.draw_text(time.ctime())
    time.sleep(0.1)


# ## Add personality to Color classifier
# Go back to the previous lesson on color classifier and train Zumi on a variety of colors. Set a happy reaction to her favorite color and sad/angry reactions to the other colors. Have a partner show Zumi various colors and try and guess what Zumi's favorite color is!
