#!/usr/bin/env python
# coding: utf-8

# ## Face Recognition
# Zumi can be trained to recognize your face! In this demo, we will give Zumi pictures of your face, have her train a model, and then run the model.
# 
# ### Step 1: Setup
# <div>
# <br/><p>In Jupyter Notebook, code is written inside boxes called "cells". You can run a cell by clicking on it, then clicking the "Run" button <img src="../Data/images/run.png" style="display: inline"> in the second toolbar.<p/>
# </div>
# 
# Try running the cell below to set up Zumi to recognize faces.

# In[ ]:


print("Cell activated!\n")
print("Now setting up Zumi...\n")

import sys
sys.path.insert(0,'../Data/demo-run')
import demo_Face_recognition as demo

print("\n\nDone!")


# <div>
# If you run into any errors, you can click the "Restart" button <img src="../Data/images/reset.png" style="display: inline"> in the second toolbar to try again. Clicking this button will force you to restart from Step 1.
# </div>
# 
# Also, did you notice the "In \[ \]:" text next to the cell? While the code in a cell is still running, there will be an asterisk inside the box, like this: "In \[\*\]:". You can tell a cell is finished because there will be a number in there instead, like this: "In \[1\]". The number is the number of cells you've ran since you started the notebook, so the first cell you run will have a "1" inside the box, the second cell will have a "2", and so on.

# ### Step 2: Collect Pictures
# 
# This cell will turn on Zumi's camera so that she can start taking pictures of faces.
# 
# * Place Zumi somewhere so that your face is level with her camera.
# * Enter your name.
# * Look into Zumi's camera, but be sure to leave enough room so she can see your face!
# * Once she sees your face, she will take a picture and remember it for later. You can tell she can see your face because a box will be drawn around it on her screen.
# * Keep looking into Zumi's camera until her screen says "Done!".

# In[ ]:


demo.collectPictures()


# Zumi can learn more than one face, by the way. Try running the cell again with a different person.

# ### Step 3: Train a Model
# 
# Once Zumi has enough pictures of faces, she will need time to learn the different faces and sort them out.
# 
# In computer language, this process is called "training". The purpose of this training is to create a "model", which Zumi will be using in the next step to recognize the faces that she learned.

# In[ ]:


demo.trainModel()


# ### Step 4: Run Model
# <div>
# <br/>
# <p>How did Zumi do? Run this cell, and Zumi will start to recognize faces using the trained model from the previous step.<p/>
# <p>Once ran, this cell will run forever. You can end it by pressing the "Stop" button <img src="../Data/images/stop.png" style="display: inline"> in the second toolbar.<p/>
# </div>

# In[ ]:


demo.runModel()


# ### Step 5: Cleanup
# 
# All done? Shutdown the camera and screen so they can be used for another demo.

# In[ ]:


demo.camera.close()
demo.screen.draw_text("")


# ### Options
# 
# These cells aren't necessary for the demo, but they may come in hand.
# 
# #### Delete One Dataset
# 
# Not satisfied with your pictures? Run this cell to remove one set of faces from Zumi's memory.

# In[ ]:


demo.deleteOneDataset()


# #### Delete All Datasets
# 
# Want to reset the demo? Run this cell to wipe Zumi's memory clean of all traces of faces.

# In[ ]:


demo.deleteAllDatasets()

