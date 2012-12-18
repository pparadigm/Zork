#!/usr/bin/env python

import startArea
import entryway
import corridor
import danceRoom
import globalvariables

print '''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMM--------MMMMMMMMMMMM--------MMMMMMM----MMMMMMMMM---MMMMMMMMMMMMM
MMMMMMMMMMMMM----MMM-----MMMMMMMMMM---MMMM----MMMMM----MMMMMM---MMMMMMMMMMMMMM
MMMMMMMMMMMM----MMMMMMM----MMMMMMMMM---MMMMMM---MMMMM----MMM---MMMMMMMMMMMMMMM
MMMMMMMMMMM----MMMMMMMMM----MMMMMMMMM---MMMMMM---MMMMMM---M---MMMMMMMMMMMMMMMM
MMMMMMMMMM----MMMMMMMMMM----MMMMMMMMMM---MMM----MMMMMMMM-------MMMMMMMMMMMMMMM
MMMMMMMMM----MMMMMMMMMM----MMMMM--MMMMM-------MMMMMMMMMMM----M----MMMMMMMMMMMM
MMMMMMMM----MMMMMMMMMM----MMMMM----MMMMM---MMM---MMMMMMMMM----MMM----MMMMMMMMM
MMMMMMM----MMMMMMMMM----MMMMMM--MM--MMMMM---MMMM----MMMMMMM----MMMMM---MMMMMMM
MMMMMM----MMMMM------MMMMMMMM--------MMMMM---MMMMMM---MMMMMM----MMMMM---MMMMMM
MMMMM-------------MMMMMMMMMM--MMMMMM--MMMMM---MMMMMM---MMMMMM----MMMM---MMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
'''
a=str(raw_input("Welcome. Would you like to begin? (Y/N/help)\n"))
if a=="y":
	startArea.startArea()
elif a=="n":
	print "Exiting..."
	exit()
elif a=="help":
	print 'All responses are typed using lowercase letters. Things you can interact with are generally indicated with capital letters. For example, a sentence that says, "The FLASHLIGHT is turned off, and the WALL behind it is unlit," indicates that you may interact with the flashlight and the wall. The command "info" reprints what information you were given when entering the room, while "describe" uses great detail to describe the room. ("Describe" and "info" commands not yet implemented.)'
elif a=="entryway":
	entryway.entryway()
elif a=="danceroom":
	danceRoom.danceRoom()
elif a=="corridor":
	corridor.corridor()
else:
	print "Error. Invalid command."
