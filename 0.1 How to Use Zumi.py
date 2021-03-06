#!/usr/bin/env python
# coding: utf-8

# <img src="../Data/images/ZumiHeader.png" width=700>

# 
# # What is Zumi?
# <font size =3>Zumi is a curious self-driving car who will learn about robotics, coding, and artificial intelligence with you!</font>
# 
# # What is AI?
#  <font size =3>AI stands for artificial intelligence. It may sound scary, but you interact with artificial intelligence every day! When Netflix makes suggestions to you or you ask Siri or Alexa how long it will take to get to your favorite restaurant, you are interacting with artificial intelligence. Artificial intelligence software is designed to appear intelligent and behave like a human, and it can do things like:
# 
# * Natural language processing. One example is anything that has a text-to-speech feature, which is when onscreen text is read out loud. This is great for anyone that is visually impaired!
# * Object classification. This is when images are classified as the correct object. Some AI machines can go even further and classify species of flowers or breeds of dogs.
# * Reasoning and problem-solving. Some AI machines are designed to play games, like Tic-Tac-Toe and Battleship, using conditionals to make their next move. For example, its logic could look like, “If my opponent puts an X in the righthand corner, I’ll put an O to its left. Else, I will put an O in the righthand corner.”
# 
# AI comes in many forms and may not always take the form of a robot. You are about to embark on a journey in which you learn about how it is applied to self-driving car technology! </font>
# 
# # How do I use Zumi?
# <font size =3>Before you dive into the world of coding and robotics, you need to learn a little bit about Zumi basics first. All of the topics will cover tips, some basic troubleshooting, and safety precautions. Use the links below to jump to a particular section.
# 
# <a href='#safety'> General Precautions</a> <br>
# <a href='#battery'> Battery Specifications and Usage</a> <br>
# <a href='#charging'> Charging Zumi</a> <br>
# <a href='#zumiboard'> Zumi Board Components (IR, Motors, and reset button)</a> <br>
# <a href='#poweroff'> Powering off</a> <br>
# 
# <hr>
# 
# <a id='safety'></a>
# ## General Precautions
# 
# * <font size =3>Avoid having wet hands when using Zumi or putting any electronics near liquids. </font>
# * <font size =3> Do not insert any metal or conductive material into the Zumi shell or near exposed circuitry.</font> 
# * <font size =3>Make sure all of the connections to Zumi are correct before powering on.</font>
# * <font size =3>Be careful not to pinch any wires when tightening bolts or standoffs.</font>
# * <font size =3>When building Zumi or connecting any components, power off Zumi. </font>
# 
# 
# <a id='battery'></a>
# ## Battery Specifications and Usage
# <font size =3>Zumi works only with a single cell Lithium Polymer battery (3.7V-4.2V). The battery has a standard JST PH 2.0MM connector.</font>
# #### Connecting the battery
# <font size =3>When connecting the battery, make sure match the red wire with the (+) on the PCB and the black wire with the (-) on the PCB. Do **not** connect the battery to any other connector on the board, or it will result in the destruction of the battery and the Zumi board.</font>
# 
# #### Removing the battery
# <font size =3>IF you need to remove the battery, grab the connector from the white plastic on the battery connector. A pair of pliers will do the job. Avoid tugging on the battery from the wires.</font>
# 
# #### Low battery
# <font size =3>When the battery is low, Zumi will begin to beep. If you do not have your MicroUSB available, make sure to turn off the switch. Failure to do this will significantly lower the power output over time. If you have your MicroUSB available, read ahead to learn how to charge Zumi.</font>
# 
# <a id='charging'></a>
# ## Charging Zumi
# <font size =3>Zumi has 2 LEDs visible on the left side of the Zumi board. These are indicators of the charging state.</font>
# 
# * <font size =3>If the RED LED is on, the battery is charging.</font>
# * <font size =3>If the BLUE LED is on, MicroUSB power has been detected.</font>
# * <font size =3>If the GREEN LED is on, the Zumi board is being powered.</font>
# * <font size =3>If **only** the GREEN led is on, then Zumi is running on battery power.</font>
# 
# #### How to charge Zumi
# <font size =3>Zumi will only be charging if the RED LED is on and the MicroUSB is connected to a power source, laptop USB port, or wall outlet USB source. If you connect the MicroUSB and the RED LED does **not** turn on, then you will need to flip the switch in order to begin charging.</font>
# 
# #### How do I know if Zumi is charged?
# <font size =3>If the switch is in the charging position ("off" position) and the RED LED is off, then the battery may be fully charged.</font>
# 
# #### Can I use Zumi while charging?
# <font size =3>You can use Zumi while charging, but the drive commands may be limited by the MicroUSB cable. If you have been using Zumi while charging and you want to disconnect the USB cable, you must first flip the switch into the "on" position. A beep will sound and the RED LED will shut off, leaving the GREEN and BLUE LEDs on. At this point you may disconnect. If you disconnect before flipping the switch, Zumi will just shut off and you will need to restart Zumi.</font>
# 
# <a id='zumiboard'></a>
# ## Zumi Board Components
# 
# <font size =3>Listed below are some general precautions relating to components connected to or on the PCB. </font>
# 
# #### Infrared (IR) LEDs
# <font size =3>The IR LEDs (especially the bottom and front LEDs) have long wires that can easily be bent, care must be taken not to bend them out of place when building zumi. Before turning zumi on, inspect that none of the pin wires are touching.</font>
# 
# #### Motors
# <font size =3>To avoid zumi’s motors from breaking, care must be taken with the small gear box. The motors have a really high reduction gear box which allows them to be very small but also very fragile. Do not force the motors to turn as this will strip the gears teeth and result in a useless motor. Avoid straining them by holding them and not allowing them to turn.
# If you Zumi appears to have problems with shutting off this may be because the motors are drawing power to quickly, you may need to lower the speed you put into the motor commands.</font>
# 
# #### Arduino reset button
# <font size =3>If Zumi won't stop running a specific code and does not appear to be responsive (motors keep driving out of control), you can reset the Arduino board by clicking the reset button located on the left side of Zumi. You can access the reset button by popping  Remember this only resets the Arduino board and not the raspberry Pi so if the pi is stuck the reset button will do nothing. Clicking the reset button makes the Arduino Zumi pre boot animation to occur.</font>
# 
# <a id='poweroff'></a>
# ## Powering off
# <font size =3>Zumi is a small computer and should be powered off correctly.
# 
# Make sure to use the dashboard in order to turn Zumi off, then wait 10 seconds before you use the switch.
# If you are using the terminal, use the ```sudo poweroff``` command, then wait for 10 seconds before you flip the switch to the "off" position.</font>
# 
