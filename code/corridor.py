import globalvariables
import entryway
import hallway1
import woodShop

def corridor():
	if globalvariables.lightsOn==0:
		print "-----"
		print "There's nothing much here. You feel the corridor extend to the WEST, but it is too dark for you too feel safe continuing on. However, you do notice a GLINT on the wall to the east. SOUTH of you is the entryway.\n"
		a = str(raw_input("What do you want to do?\n"))
		if a=="go back" or a=="return entryway" or a=="south":
			print "-----"
			print "You head to the ENTRYWAY."
			entryway.entryway()
		elif a=="examine glint" or a=="look glint" or a=="glint":
			glint()
		elif a=="continue" or a=="west":
			print "-----"
			print "Your gut tells you that you are likely to be eaten by a grue. You return to the slightly lighter area."
			corridor()
		else:
			print "-----"
			print "You don't think you can do that."
			corridor()
	elif globalvariables.lightsOn==1:
		print "-----"
		print "There is a long HALLWAY to the west with many doors on either side. Nearby and also to the west is a PURPLEDOOR that you could not see in the darkness.\n"
		a = str(raw_input("What do you want to do?\n"))
		if a=="go back":
			print "-----"
			print "You turn around and head back to the ENTRYWAY."
			entryway.entryway()
		elif a=="continue" or a=="hallway":
			print "-----"
			print "You continue on a few steps, into the hallway."
			hallway1.hallway1()
		elif a=="purpledoor":
			if globalvariables.chisel==0:
				print "-----"
				print "The purpledoor is painted shut."
				corridor()
			elif globalvariables.chisel==1 and globalvariables.woodShopDoorOpen==0:
				purpledoor()
			elif globalvariables.chisel==1 and globalvariables.woodShopDoorOpen==1:
				print "-----"
				print "You step through the purpledoor and into the WOODSHOP."
				woodShop.woodShop()
			else:
				print "Error: problem with the chisel or the woodshop door."
				corridor()
		else:
			print "-----"
			print "You don't think you can do that."
			corridor()
	else:
		print "Error: The lights are broken somehow!"
			
def purpledoor():
	print "-----"
	print "The purpledoor is painted shut."
	a=str(raw_input("Would you like to use your chisel on it?\n"))
	if a=="yes" or a=="y": 
		print "-----"
		print "You use your chisel on the door. You try the knob, and the door opens."
		woodShop.woodShop()
	elif a=="no" or a=="n":
		print "-----"
		print "You don't use your chisel on the door."
		corridor()
	else:
		print "That is not a proper answer."
		purpledoor()
		
def glint():
	if globalvariables.buttonPressable==0:
		print "-----"
		print "You examine the glint. Up close, you can barely see that it is a metal object attached to the wall. You run your fingers over it. It's cold, but you also feel something similar to a BUTTON. Alongside the BUTTON is a SLIT.\n"
		a=str(raw_input("What do you want to do?\n"))
		if a=="leave" or a=="go back":
			print "-----"
			print "You step away from the glint."
			corridor()
		elif a=="push button" or a=="press button" or a=="button":
			print "-----"
			print "You press the button, but to your dissatisfaction, nothing happens."
			glint()
		elif a=="examine slit" or a=="look slit" or a=="slit":
			slit()
		elif a=="finger slit":
			print "-----"
			print "Why would you want to do that?"
			glint()
		else:
			print "-----"
			print "You don't think you can do that."
			glint()
	elif globalvariables.buttonPressable==1:
		print "-----"
		print "You examine the glint. Close up, you can see that there is a BUTTON. Alongside the BUTTON is a slit filled with a key.\n"
		a=str(raw_input("What do you want to do?\n"))
		if a=="leave" or a=="go back":
			print "-----"
			print "You step away from the GLINT."
			corridor()
		elif a=="push button" or a=="press button" or a=="button":
			globalvariables.buttonPressable=0
			print "-----"
			print "The lights turn on. You can now see the long hallway to the WEST of you, with doors every few feet on both sides. You now feel safe to CONTINUE down the hallway."
			globalvariables.lightsOn=1
			corridor()
		elif a=="examine slit" or a=="look slit" or a=="slit":
			slit()
		else:
			print "-----"
			print "You don't think you can do that."
			glint()
def slit():
	if globalvariables.keyAccess==0 and globalvariables.lightKey==0:
		print "-----"
		print "You try to garner more information about the slit. All you can tell is that it is a small rectangle. A key of some sort might fit."
		globalvariables.keyAccess=1
		glint()
	elif globalvariables.keyAccess==1:
		print "-----"
		print "A key might fit in this slit. I should look for one."
		glint()
	elif globalvariables.keyAccess==0 and globalvariables.lightKey==1:
		print "-----"
		print "A key might fit here." 
		a=str(raw_input("Would you like to try your key?\n"))
		if a=="yes" or a=="y":
			print "-----"
			print "You insert your key."
			globalvariables.buttonPressable=1
			globalvariables.lightKey=0
			glint()
		elif a=="no" or a=="n":
			print "-----"
			print "You don't insert your key."
			glint()
		else: 
			print "-----"
			print "That is not a proper answer."
			slit()
	else:
		print "-----"
		print "Error with variable storage."
		glint()
