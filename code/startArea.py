import entryway

def startArea():
	print "You find yourself lying a cold, linoleum floor. Everything is silent. It's dark, but there is some light filtering in above you.\n"
	a=str(raw_input("What do you want to do?\n"))
	if a=="stand":
		print "You stand up. Now you have a better bearing of your surroundings. It is clear that you are inside of a building.\n" 
		entryway.entryway()
	elif a=="die":
		print "Fine, if your will to live is that minimal."
		exit()
	elif a=="import flashlight":
		print "If only you had a huge shoulderbag and green jacket. However, you do not. You find that you are unable to import a flashlight.\n"
		startArea()
	else:
		print "Perhaps you should STAND before you do that.\n"
		startArea()
