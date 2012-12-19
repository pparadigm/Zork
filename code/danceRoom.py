import globalvariables

def danceFloor(): 
	print "-----"
	print "The wall to the east of you is made of MIRRORs, and an ELECTRICFAN sits in the corner of the dance floor. To the SOUTH is another door, and there is more of the room to the WEST that you can't see.\n"
	a=str(raw_input("What do you want to do?\n"))
	if a=="dance":
		dance()
	elif a=="mirror":
		print "-----"
		print "You discover that you're tall and scrawny and male. You realize you're wearing a soft, blue jacket, and khaki pants. You turn away quickly, it feels weird for you to be examining your reflection."
		danceFloor()
	elif a=="electricfan":
		print "-----"
		print "You move over to the ELECTRICFAN."
		electricFan()
	elif a=="west":
		print "-----"
		print "You move to the WEST section of the room, to the DANCEROOM proper."
		danceRoom()
	else:
		print "-----"
		print "You don't think you can do that."
		danceFloor()
		
def dance():
	print "-----"
	print "Some lyrics come to mind."
	a=random.randrange(1, 4)
	if str(a)=="1":
		print "\nWe can dance if we want to,\nwe can leave your friends behind.\n'Cuz your friends don't dance,\nand if they don't dance,\nwell they're no friends of mine.\n"
		danceFloor()
	elif str(a)=="2":
		print "\nWhere you go I go.\nWhat you see, I see.\nI know I'a never be me\nwithout the security\nof your loving arms\nkeeping me from harm.\nPut your hand in my hand, and we'll stand.\n"
		danceFloor()
	elif str(a)=="3":
		print "\nCome close, come close\nand call my name.\nHow can you turn your back on me\nwhen you know my pain?\n\nStay close, stay close,\nlight up the night.\nSave me from the part of me\nthat's begging to die.\n"
		danceFloor()
	elif str(a)=="4":
		print "\nIt's the last night on earth,\nbefore the great divide.\nMy hands are shaking,\ntime was never on our side.\n\nAnd there's no such thing\nas a beautiful goodbye,\nas and ordinary day.\nI prayed for you a thousand times.\n"
		danceFloor()
	else:
		print "Error: random number generated outside of limits."
		danceFloor()
		
def electricFan():
	print "-----"
	print "The ELECTRICFAN has a chipped blade, but other than that it is intact. Its cord is still plugged into the wall socket.\n"
	a=str(raw_input("What do you want to do?\n"))
	if a=="turn on fan" or a=="turn on electricfan":
		print "-----"
		print "You turn up the power knob on the ELECTRICFAN. Nothing happens. You reset the knob."
		electricFan()
	elif a=="take electricfan" or a=="take fan":
		print "-----"
		print "You unplug the ELECTRICFAN and pick it up. You note that you won't be able to do things with other objects while you are carrying the ELECTRICFAN."
		globalvariables.electricfan=1
		danceFloor()
	elif a=="leave" or a=="go back":
		print "-----"
		print "You step back from the ELECTRICFAN."
		danceFloor()
	else:
		print "-----"
		print "You don't think you can do that."
		electricFan()
		
		
def danceRoom():
	print "-----"
	print "You are back on linoleum flooring. To the west are more mirrors, and to the south is a short hall. In the WEST side of the hall, you can see a door. Opposite the door are rows and rows of pictures. There is also another door at the SOUTH end of the hall. To the EAST of you, is, of course, the DANCEFLOOR.\n"
	a=str(raw_input("What do you want to do?\n"))
	if a=="west":
		print "-----"
		print "You walk through the door, into an OFFICE."
		office()
	elif a=="south":
		print "-----"
		print "You approach the door at the end of the hallway."
		exitProper()
	elif a=="east":
		print "-----"
		print "You decide to return to the DANCEFLOOR."
		danceFloor()
	else:
		print "-----"
		print "You don't think you can do that."
		danceRoom()
		
def office():
	print "-----"
	print "some description here" #later, also decide ifs and elifs.
	danceRoom()
	
def exitProper():
	print "-----"
	print "description of door, and why you can't physically open it. You return to the DANCEROOM."
	danceRoom()
