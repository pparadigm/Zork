#!/usr/bin/env python
import random

#def example(): ex
	#print "description"
	#ex=str(raw_input("What do you want to do?\n"))
	#if ex=="action":
		#print "decription"
		#callroom()
	#elif ex=="otheraction":
		#print "decription"
		#callroom()
	#else:
		#print "error statement"
		#callroom()
		
		
'''
def myHandler(callingParams): action
	print("view of room")
	if callingParams is not None:
		action = str(raw_input("prompt"))
	else: action=callingParams
	
	if action=="some_val":
		do stuff
		return new_place
'''
'''
then in your main program, you have a large case that does this:

#select room

place="start"

while place is not None:
	if place=="start": place=start(callingParams)
	elif place=="some_other_place": place=another_place(callingParams)

#all you have to do to end game is to return nothing, and you will get out of the Nav loop
#then the code outside will run

print("you won!")
'''

#also, local vars are local, uniqueness doesn't matter, and if you insist on using them in this way, you should use the same name
#throughout the program, such as action

#def woodShop(): wS
	
#def woodRoom(): wR

#def paint(): p

#def supplies(): s

#def project(): pro

#def ???(): ?
	
#def metalShop(): mS

#def forge(): f

#def cage(): cg

#def cave(): cv
	
def danceFloor(): 
	print "The wall to the east of you is made of MIRRORs, and an ELECTRICFAN sits in the corner of the dance floor. To the SOUTH is another door, and there is more of the room to the WEST that you can't see."
	dF=str(raw_input("What do you want to do?\n"))
	if dF=="dance":
		dance()
	elif dF=="mirror":
		print "You discover that you're tall and scrawny and male. You realize you're wearing a soft, blue jacket, and khaki pants. You turn away quickly, it feels weird for you to be examining your reflection."
		danceFloor()
	elif dF=="electricfan":
		print "You move over to the ELECTRICFAN."
		electricFan()
	elif dF=="west":
		print "You move to the WEST section of the room, to the DANCEROOM proper."
		danceRoom()
	else:
		print "You don't think you can do that."
		danceFloor()
		
def dance():
	print "Some lyrics come to mind."
	d=random.randrange(1, 4)
	if str(d)=="1":
		print "\nWe can dance if we want to,\nwe can leave your friends behind.\n'Cuz your friends don't dance,\nand if they don't dance,\nwell they're no friends of mine.\n"
		danceFloor()
	elif str(d)=="2":
		print "\nWhere you go I go.\nWhat you see, I see.\nI know I'd never be me\nwithout the security\nof your loving arms\nkeeping me from harm.\nPut your hand in my hand, and we'll stand.\n"
		danceFloor()
	elif str(d)=="3":
		print "\nCome close, come close\nand call my name.\nHow can you turn your back on me\nwhen you know my pain?\n\nStay close, stay close,\nlight up the night.\nSave me from the part of me\nthat's begging to die.\n"
		danceFloor()
	elif str(d)=="4":
		print "\nIt's the last night on earth,\nbefore the great divide.\nMy hands are shaking,\ntime was never on our side.\n\nAnd there's no such thing\nas a beautiful goodbye,\nas and ordinary day.\nI prayed for you a thousand times.\n"
		danceFloor()
	else:
		print "Error: random number generated outside of limits."
		danceFloor()
		
def electricFan():
	print "The ELECTRICFAN has a chipped blade, but other than that it is intact. Its cord is still plugged into the wall socket."
	eF=str(raw_input("What do you want to do?\n"))
	if eF=="turn on fan" or eF=="turn on electricfan":
		print "You turn up the power knob on the ELECTRICFAN. Nothing happens. You reset the knob."
		electricFan()
	elif eF=="take electricfan" or eF=="take fan":
		print "You unplug the ELECTRICFAN and pick it up. You note that you won't be able to do things with other objects while you are carrying the ELECTRICFAN." #need new description for dance floor when ELECTRICFAN is in possession, possibly create an "inventory" and check that when entering rooms?
		danceFloor()
	elif eF=="leave" or eF=="go back":
		print "You step back from the ELECTRICFAN."
		danceFloor()
	else:
		print "You don't think you can do that."
		electricFan()
		
		
def danceRoom():
	print "You are back on linoleum flooring. To the west are more mirrors, and to the south is a short hall. In the WEST side of the hall, you can see a door. Opposite the door are rows and rows of pictures. There is also another door at the SOUTH end of the hall. To the EAST of you, is, of course, the DANCEFLOOR."
	dR=str(raw_input("What do you want to do?\n"))
	if dR=="west":
		print "You walk through the door, into an OFFICE."
		office()
	elif dR=="south":
		print "You approach the door at the end of the hallway."
		exitProper()
	elif "east":
		print "You decide to return to the DANCEFLOOR."
		danceFloor()
	else:
		print "You don't think you can do that."
		danceRoom()
		
def office():
	print "some description here" #later, also decide ifs and elifs.
	danceRoom()
	
def exitProper():
	print "description of door, and why you can't physically open it. You return to the DANCEROOM."
	danceRoom()
	
	
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
	elif sA=="warp fan":
		print "You move over to the ELECTRICFAN."
		electricFan()
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
