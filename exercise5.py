# - *- coding: utf- 8 - *-

def kilostopounds(kilos):
	return float(kilos) * 2.441933

def poundstokilos(pounds):
	return float(pounds) / 2.441933

def inchestocentimeters(inches):
	return float(inches) * 2.54

def centimeterstoinches(centimeters):
	return float(centimeters) / 2.54

name   = "Zed A.Shaw"
age    = 35          # not a lie
height = 74          # inches
weight = 180         # lbs
eyes   = "Blue"
teeth  = "White"
hair   = "Brown"

print "Let's talk about %s."  % name
print "He's %d inches tall."  % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)

print "%f inches = %f centimeters" % (height, inchestocentimeters(height))
print "%f pounds = %f kilos" % (weight, poundstokilos(weight))

