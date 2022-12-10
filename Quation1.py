import re

def isValid(s):
	
	Pattern = re.compile("^(\+\d{212}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
	return Pattern.match(s)

s = "+212-456-7890"
if (isValid(s)):
	print ("Valid Number")	
else :
	print ("Invalid Number")