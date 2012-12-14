#!/usr/bin/python
from random import randint


#def woodShop(): wS

#def woodRoom():

#def paint():

#def supplies():

#def project():

#def ???():
	
#def metalShop(): mS

#def forge():

#def cage():

#def cave():
	
def danceFloor(): 
	print "The wall to the east of you is made of MIRRORs, and an ELECTRICFAN sits in the corner of the dance floor. To the SOUTH is another door, and there is more of the room to the WEST that you can't see."
	dF=str(raw_input("What do you want to do?\n"))
	if dF=="dance":
		dance()
	elif dF=="mirror":
		print "You discover that you're tall and scrawny and male. You turn away quickly, it feels weird for you to be examining your reflection."
		danceFloor()
	else:
		print "You don't think you can do that."
		danceFloor()
		
def dance():
	print "Some lyrics come to mind."
	d=randint(1, 3+1)
	if d=="1":
		print "\nWe can dance if we want to,\nwe can leave your friends behind.\n'Cuz your friends don't dance,\nand if they don't dance,\nwell they're no friends of mine.\n"
		danceFloor()
	elif d=="2":
		print "\nWhere you go I go.\nWhat you see, I see.\nI know I'd never be me\nwithout the security\nof your loving arms\nkeeping me from harm.\nPut your hand in my hand, and we'll stand.\n"
		danceFloor()
	elif d=="3":
		print "\nCome close, come close\nand call my name.\nHow can you turn your back on me\nwhen you know my pain?\n\nStay close, stay close,\nlight up the night.\nSave me from the part of me\nthat's begging to die.\n"
		danceFloor()
	elif d=="4":
		print "\nIt's the last night on earth,\nbefore the great divide.\nMy hands are shaking,\ntime was never on our side.\n\nAnd there's no such thing\nas a beautiful goodbye,\nas and ordinary day.\nI prayed for you a thousand times.\n"
		danceFloor()
	else:
		print "Error: random number generated outside of limits."
		danceFloor()
		
#def danceRoom(): dR
	
#def bertucciLand(): bL
	
#def paceYourself(): pY
	
#def earnHarts(): eH
	
#def fridge():
	
#def ladies(): lD
	
#def m(): m
	
#def fennellCorner(): fC
	
#def walkersHideout(): wH
	
#def seamsSuspect(): sS
	
#def sciO(): sO

#def clo(): c
	
#def janitorsCloset(): jC

#def subBasement(): sB

#def loft(): l
	
#def elecRoom(): eR
	
#def pltw(): p
	
#def codeRoom(): cR
	
#def gymDoors(): gD

#def hallOne(): h1

#def hallTwo(): h2

#def hallThree(): h3
	
def startArea():
	print "You find yourself lying a cold, linoleum floor. Everything is silent. It's dark, but there is some light filtering in above you."
	sA=str(raw_input("What do you want to do?\n"))
	if sA=="stand":
		print "You stand up. Now you have a better bearing of your surroundings. It is clear that you are inside of a building." 
		entryway()
	elif sA=="die":
		print "Fine, if your will to live is that minimal."
		exit()
	elif sA=="import flashlight":
		print "If only you had a huge shoulderbag and green jacket. However, you do not. You find that you are unable to import a flashlight."
		startArea()
	elif sA=="warp dancefloor":
		print "You open the door and enter into an alcove. Ahead is a wooden floor. You step onto it and realize that it is a DANCEFLOOR. You walk to the center of the wood floor."
		danceFloor()
	else:
		print "Perhaps you should STAND before you do that."
		startArea()

def entryway():
	print "In front of you are two paths: the right one leads to a STAIRCASE, and the left one turns off into a CORRIDOR. Behind you is a set of DOORs surrounded by WINDOWs. You find yourself standing on a MAT."
	#need descriptions for both ways of travel (or directions that aren't relative, but absolute), and a management system
	e = str(raw_input("What do you want to do?\n"))
	if e=="lay down":
		print "You lay back down on the linoleum floor."
		startArea()
	if e=="staircase":
		print "You walk up the STAIRCASE. As you near the top, however, an unbearable sense of foreboding overcomes you, and you are forced to turn around and go back. You return to the ENTRYWAY."
		entryway()
	elif e=="look window" or e=="examine window":
		print "You go up to the WINDOW and look out through it. It's dark outside of the building. Everything is still and empty, trees sit without leaves. Before you lies a street; there are rusty signs along the edge of it, and sagging buildings in the distance. You get the chills. You turn back to face the CORRIDOR."
		entryway() 
	elif e=="corridor":
		print "You step forward, into the CORRIDOR."
		corridor()
	elif e=="open door" or e=="try door" or e=="unlock door":
		print "You don't want to do that. The outside gives you the chills, and not from the cold. You turn back to face the CORRIDOR."
		entryway()
	elif e=="examine door" or e=="look door":
		print "The DOORs look old but sturdy. They're made with metal, the paint is peeling off. They have small slits for windows filled with reinforced glass. You turn back to face the CORRIDOR."
		entryway()
	elif e=="look mat" or e=="examine mat":
		print "A dirty, tattered MAT meant for the cleaning of shoes. There is nothing of interest here. You turn back to the CORRIDOR."
		entryway()
	else:
		print "You don't think you can do that."
		entryway()
		
def corridor():
	print "There's nothing much here. You feel the CORRIDOR extend to your left, but it is too dark for you too feel safe continuing on. However, you do notice a GLINT on the wall before you."
	c = str(raw_input("What do you want to do?\n"))
	if c=="go back" or c=="return entryway":
		print "You turn around and head back to the ENTRYWAY."
		entryway()
	elif c=="examine glint" or c=="look glint":
		glint()
	else:
		print "You don't think you can do that."
		glint()
		
def glint():
	print "You examine the GLINT. Up close, you can barely see that it is a metal object attached to the wall. You run your fingers over it. It's cold, but you also feel something similar to a BUTTON. Alongside the BUTTON is a SLIT."
	g=str(raw_input("What do you want to do?\n"))
	if g=="leave" or g=="go back":
		print "You step away from the GLINT."
		corridor()
	elif g=="push button" or g=="press button":
		print "To your dissatisfaction, nothing happens."
		glint()
	elif g=="examine slit" or g=="look slit":
		print "You try to garner more information about the slit. All you can tell is that it is small."
		glint()
	elif g=="finger slit":
		print "Why would you want to do that?"
		glint()
	#need to figure out how to use KEY with SLIT. if player does not have the KEY, they shouldn't be able to use the KEY, obviously. need to also figure out how to make the MAT accessible. maybe this is what maldridge meant about a state machine.
	else:
		print "You don't think you can do that."
		glint()
			
startArea()
