#!/usr/bin/env python

import startArea
import entryway
import corridor
import danceRoom

print '''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMM--------MMMMMMMMMM--------MMMMMMM----MMMMMMMMM---MMMMMMMMMMMMM
MMMMMMMMMMMMM----MMM-----MMMMMMMM---MMMM----MMMMM----MMMMMM---MMMMMMMMMMMMMM
MMMMMMMMMMMM----MMMMMMM----MMMMMMM---MMMMMM---MMMMM----MMM---MMMMMMMMMMMMMMM
MMMMMMMMMMM----MMMMMMMMM----MMMMMMM---MMMMMM---MMMMMM---M---MMMMMMMMMMMMMMMM
MMMMMMMMMM----MMMMMMMMMM----MMMMMMMM---MMM----MMMMMMMM-------MMMMMMMMMMMMMMM
MMMMMMMMM----MMMMMMMMMM----MMM--MMMMM-------MMMMMMMMMMM----M----MMMMMMMMMMMM
MMMMMMMM----MMMMMMMMMM----MMM----MMMMM---MMM---MMMMMMMMM----MMM----MMMMMMMMM
MMMMMMM----MMMMMMMMM----MMMM--MM--MMMMM---MMMM----MMMMMMM----MMMMM---MMMMMMM
MMMMMM----MMMMM------MMMMMM--------MMMMM---MMMMMM---MMMMMM----MMMMM---MMMMMM
MMMMM-------------MMMMMMMM--MMMMMM--MMMMM---MMMMMM---MMMMMM----MMMM---MMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
'''
a=str(raw_input("Welcome. Would you like to begin? (Y/N)\n"))
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
