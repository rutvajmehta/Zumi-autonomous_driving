#!/usr/bin/env python
# coding: utf-8

# ## Emote & React
# Zumi can read your emotions. Run this demo to see how she reacts to you being happy or sad.
# 
# ### Step 1: Setup
# <div>
# <br/><p>In Jupyter Notebook, code is written inside boxes called "cells". You can run a cell by clicking on it, then clicking the "Run" button <img src="../Data/images/run.png" style="display: inline"> in the second toolbar.<p/>
# </div>
# 
# Try running the cell below to set up Zumi to recognize emotions.

# In[ ]:


print("Cell activated!\n")
print("Now setting up Zumi...\n")

import sys
sys.path.insert(0,'../Data/demo-run')
import demo_Smile_reaction as demo

print("\n\nDone!")


# <div>
# If you run into any errors, you can click the "Restart" button <img src="../Data/images/reset.png" style="display: inline"> in the second toolbar to try again. Clicking this button will force you to restart from Step 1.
# </div>
# 
# Also, did you notice the "In \[ \]:" text next to the cell? While the code in a cell is still running, there will be an asterisk inside the box, like this: "In \[\*\]:". You can tell a cell is finished because there will be a number in there instead, like this: "In \[1\]". The number is the number of cells you've ran since you started the notebook, so the first cell you run will have a "1" inside the box, the second cell will have a "2", and so on.
# 
# ### Step 2: Play with Zumi
# 
# Now that Zumi has been set up, run the cell below to see how she reacts to your facial expressions.
# 
# * Place Zumi somewhere so that your face is level with the camera.
# * Place your nose in front of the camera, but leave a small gap in between you and Zumi. Otherwise, she can’t see your whole face and can’t detect your emotions. 
# * Try grinning or frowning in front of Zumi. If Zumi can find your face, she will react.
# * <div>You can end the demo by pressing the "Stop" button <img src="../Data/images/stop.png" style="display: inline"> in the second toolbar.</div>

# In[ ]:


demo.run()

