#!/usr/bin/env python
import sys
def startArea():
	print "You wake up on a cold, linoleum floor. Everything is silent. It's dark, but there is some light filtering in above you."
	sA = str(raw_input("What do you want to do?\n"))
	if sA == "stand":
		print "You stand up. Now you have a better bearing of your surroundings. It is clear that you are inside of a building." 
		entryway()
	else:
		print "Perhaps I should STAND before I do that."
		startArea()

def entryway():
	print "In front of you are two paths: the RIGHT one leads to a staircase, and the LEFT one turns off into a corridor. Behind you is a set of DOORs surrounded by WINDOWs."
	e = str(raw_input("What do you want to do?\n"))
	if e == "go right" or e=="walk right":
		print "You walk up the staircase. As you near the top, however, an unbearable sense of foreboding overcomes you, and you are forced to turn around and go back.\nYou return to the ENTRYWAY."
		entryway()
	elif e == "look window" or e=="examine window":
		print "You go up to the window and look out of it. It's dark outside of the building. Everything is still and empty, trees sit without leaves. Before you lies a street; there are rusty signs along the edge of it, and sagging buildings in the distance. You get the chills. You turn back to face the corridor."
		entryway() 
	elif e == "go left" or e=="walk left":
		print "DANCE PARTAY!"
	elif e == "open door" or e=="try door" or e=="unlock door" or e=="examine door":
		print "I don't want to do that. The outside gives me the chills, and not from the cold."
		print "You turn back to face the corridor."
		entryway()
	else:
		print "I don't think I can do that."
		entryway()
		
startArea()
