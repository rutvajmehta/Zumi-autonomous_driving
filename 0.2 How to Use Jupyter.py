#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# # What is Jupyter Notebook?
# 
# Jupyter Notebook is an environment where you can write and test code. You can also include descriptive text (like what you're reading right now!) to describe your code. Many researchers use it to write up their reports with embedded code examples that you can run and test for yourself. In the following lessons you will be using the Python programming language. However, Jupyter Notebook supports over 40 programming languages!
# 
# <img src="../Data/images/Jupyter.png" width=400>
# 
# ## Opening Jupyter Notebook
# When you first open Jupyter, you will see a screen similar to the one above. It shows you a list of all your current notebooks. The picture shows the different parts of the home screen. To open a notebook, click on the name of the notebook you would like to open. The color of the notebook icon will indicate which notebooks are already open. 
# 
# <img src="../Data/images/JupyterHome.png">
# 
# ## Inside a Jupyter notebook
# 
# You write the code for your Zumi inside Jupyter Notebook. When you open a lesson, you should already see cells filled with text and code. To go through the lesson, you will need to run code, stop code, and save your changes! The most important tools that you will use are highlighted for you below:
# 
# <img src="../Data/images/jupyter_toolbar.png">
# 
# <hr>
# 
# ## Cells
# 
# A typical Jupyter notebook is divided into cells. Some cells have text, such as the one you are currently reading, and some cells can run code. 
# 
# ### Running code
# The cell below is an example of a code cell. To run the cell and execute code, select it so that is highlighted in <span style="color:dodgerblue">blue </span> or <span style="color:#52BE80">green </span>. For future reference, a cell outline in blue is selected but not in edit mode. A cell outlined is green is selected and in edit mode. In either state, you can click "Run" in the toolbar or press ```Shift``` + ```Enter```.

# In[2]:


print("This is a code cell!")


# After you run a cell, the output of the code will appear below it. The number next to the cell will also change from ```In [ ]``` to ```In [1]```. The number indicates the order that the cells executed and completed their processes. In Jupyter Notebook, you can run either all cells or sections of your code at a time! Try running the above code again and it will change from ```In [1]``` to ```In [2]```.
# 
# If the ```In [ ]``` indicator does not appear next to a cell, that cell **cannot** run code. For example, try "running" the cell below.
# 

# print("This is not a code cell")

# This cell was formatted into text instead. These cells are called **markdown** cells. Sometimes you can switch your cell into a different type by accident. If this happens, go to ```Cell > Cell Type``` in the toolbar to switch between the two. Try changing the cell above from markdown to code.
# 
# 
# ### Stopping the code
# Sometime you need to stop the code that is currently running. Maybe you have a while loop that is going forever and you are trying to escape! Next to the "Run" button in the toolbar you will find a black square. This is the stop button and will terminate the cell that is running. Run the cell below (which runs forever) and then stop the code.

# In[3]:


count=0
while True:
    print(count)
    count+=1
    


# Did you notice while the cell is running there's an **asterisk** next to the cell? It looks like this: ```In [*]```. Any cell with an asterisk is still running. 
# 
# ### Adding cells
# If you want to create a new cell, go to the toolbar and click ```Insert```. In the menu you have options to insert a cell above or below the current cell.
# 
# <img src="../Data/images/adding_cells.png">
# 
# ### Deleting cells
# 
# Under ```Edit``` in the toolbar, you will find many tools including "Delete Cells". This will delete any cells that are currently selected.
# 
# <img src="../Data/images/deleting_cells.png">
# 
# ### Locked cells
# Some cells that you see on tutorials (including this one) are locked. This means that you can't delete or edit them. Try editing the different cells below. You shouldn't be able to edit some of them.
# 
# 

# # I can be edited and deleted

# # I can be edited, but I can't be deleted

# # I can't be edited or deleted

# <hr>
# 
# ## Notebook functions
# 
# ### Restarting a notebook
# There may be times when you want to clear all of the output from your cells and restart all of your code. In the toolbar there is a tab called ```Kernel```, and in its menu you will see an option to ```Restart & Clear Output```. Once you select it, all of the output will be erased and those cells will be ready to be run again! You can double check by looking for empty ```In[]``` brackets. 
# 
# <img src="../Data/images/restart_notebook.png">
# 
# ### Shutting down a Jupyter Notebook
# Even if you close the tab, a notebook will remain open until shutdown. It is recommended you leave only one notebook open at a time. To shut down a notebook, select it and click on the orange "Shutdown" button. Be careful not to delete it by accident!
# 
# <img src="../Data/images/shutdown_notebook.png">
# 
# These are all the basics you need to know to run the lessons in Jupyter Notebook. Head on over to Lesson 1.1 to start learning!
