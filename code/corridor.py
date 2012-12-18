import entryway

def corridor():
	print "There's nothing much here. You feel the CORRIDOR extend to your left, but it is too dark for you too feel safe continuing on. However, you do notice a GLINT on the wall before you."
	c = str(raw_input("What do you want to do?\n"))
	if c=="go back" or c=="return entryway":
		print "You turn around and head back to the ENTRYWAY."
		entryway.entryway()
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
