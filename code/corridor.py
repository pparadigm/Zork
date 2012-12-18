import globalvariables
import entryway

def corridor():
	print "-----"
	print "There's nothing much here. You feel the CORRIDOR extend to your left, but it is too dark for you too feel safe continuing on. However, you do notice a GLINT on the wall before you.\n"
	a = str(raw_input("What do you want to do?\n"))
	if a=="go back" or a=="return entryway":
		print "-----"
		print "You turn around and head back to the ENTRYWAY."
		entryway.entryway()
	elif a=="examine glint" or a=="look glint" or a=="glint":
		glint()
	elif a=="continue"
		print "-----"
		print "Your gut tells you that you are likely to be eaten by a grue. You return to the light."
		corridor()
	else:
		print "-----"
		print "You don't think you can do that."
		corridor()
		
def glint():
	print "-----"
	print "You examine the GLINT. Up close, you can barely see that it is a metal object attached to the wall. You run your fingers over it. It's cold, but you also feel something similar to a BUTTON. Alongside the BUTTON is a SLIT.\n"
	a=str(raw_input("What do you want to do?\n"))
	if a=="leave" or a=="go back":
		print "-----"
		print "You step away from the GLINT."
		corridor()
	elif a=="push button" or a=="press button" or a=="button":
		print "-----"
		print "To your dissatisfaction, nothing happens."
		glint()
	elif a=="examine slit" or a=="look slit" or a=="slit":
		print "-----"
		print "You try to garner more information about the slit. All you can tell is that it is a small rectangle. A key of some sort might fit."
		glint()
	elif a=="finger slit":
		print "-----"
		print "Why would you want to do that?"
		glint()
	#need to figure out how to use KEY with SLIT. if player does not have the KEY, they shouldn't be able to use the KEY, obviously. need to also figure out how to make the MAT accessible. maybe this is what maldridge meant about a state machine.
	else:
		print "-----"
		print "You don't think you can do that."
		glint()
