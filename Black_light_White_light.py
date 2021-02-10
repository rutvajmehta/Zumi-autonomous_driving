#!/usr/bin/env python
# coding: utf-8

# ## Black Light, White Light
# Zumi can recognize simple colors. In this demo, we will control Zumi using black and white cards.
# 
# ### Step 1: Setup
# <div>
# <br/><p>In Jupyter Notebook, code is written inside boxes called "cells". You can run a cell by clicking on it, then clicking the "Run" button <img src="../Data/images/run.png" style="display: inline"> in the second toolbar.<p/>
# </div>
# 
# Try running the cell below to set up Zumi to recognize black and white.

# In[ ]:


print("Cell activated!\n")
print("Now setting up Zumi...\n")

import sys
sys.path.insert(0,'../Data/demo-run')
import demo_BW_light as demo

print("\n\nDone!")


# <div>
# If you run into any errors, you can click the "Restart" button <img src="../Data/images/reset.png" style="display: inline"> in the second toolbar to try again. Clicking this button will force you to restart from Step 1.
# </div>
# 
# Also, did you notice the "In \[ \]:" text next to the cell? While the code in a cell is still running, there will be an asterisk inside the box, like this: "In \[\*\]:". You can tell a cell is finished because there will be a number in there instead, like this: "In \[1\]". The number is the number of cells you've ran since you started the notebook, so the first cell you run will have a "1" inside the box, the second cell will have a "2", and so on.
# 
# ### Step 2: Play with Zumi
# 
# Now that Zumi has been set up, run the cell below to start controlling Zumi.
# 
# * Place Zumi somewhere so she can move around.
# * Once the demo starts, place a white or black card in front of Zumi, and press enter.
# * A white card will make Zumi go forward, while a black card will make her stop.
# * <div>You can end the demo by pressing the "Stop" button <img src="../Data/images/stop.png" style="display: inline"> in the second toolbar, or by typing "q" before pressing enter.</div>

# In[ ]:


demo.run()

