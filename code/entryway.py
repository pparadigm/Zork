import corridor
import startArea

def entryway():
	print "In front of you are two paths: the right one leads to a STAIRCASE, and the left one turns off into a CORRIDOR. Behind you is a set of DOORs surrounded by WINDOWs. You find yourself standing on a MAT."
	#need descriptions for both ways of travel (or directions that aren't relative, but absolute), and a management system
	a=str(raw_input("What do you want to do?\n"))
	if a=="lay down":
		print "You lay back down on the linoleum floor."
		startArea.startArea()
	if a=="staircase":
		print "You walk up the STAIRCASE. As you near the top, however, an unbearable sense of foreboding overcomes you, and you are forced to turn around and go back. You return to the ENTRYWAY."
		entryway()
	elif a=="look window" or a=="examine window":
		print "You go up to the WINDOW and look out through it. It's dark outside of the building. Everything is still and empty, trees sit without leaves. Before you lies a street; there are rusty signs along the edge of it, and sagging buildings in the distance. You get the chills. You turn back to face the CORRIDOR."
		entryway() 
	elif a=="corridor":
		print "You step forward, into the CORRIDOR."
		corridor.corridor()
	elif a=="open door" or a=="try door" or a=="unlock door":
		print "You don't want to do that. The outside gives you the chills, and not from the cold. You turn back to face the CORRIDOR."
		entryway()
	elif a=="examine door" or a=="look door" or a=="door":
		print "The DOORs look old but sturdy. They're made with metal, the paint is peeling off. They have small slits for windows filled with reinforced glass. You turn back to face the CORRIDOR."
		entryway()
	elif a=="look mat" or a=="examine mat" or "mat":
		print "A dirty, tattered MAT meant for the cleaning of shoes. There is nothing of interest here. You turn back to the CORRIDOR."
		entryway()
	else:
		print "You don't think you can do that."
		entryway()
