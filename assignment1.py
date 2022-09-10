import re

# create regular expression
regexWithHyphen = re.compile("^[4|5|6][0-9]{3,3}-[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}$")
regexWithoutHyphen=re.compile("^[4|5|6][0-9]{15,15}$")

# ask user input account number
accountNo=input("Please enter your account number: ")

# compare the inputed acc no to the regex
if regexWithHyphen.match(accountNo) or regexWithoutHyphen.match(accountNo) :

	# remove '-' if any
	accountNo=accountNo.replace('-', '')

	# init repeat flag with boolean value false
	repeat=False

	#  for check consecutive digits repeating 4 or more times
	for i in range(0, len(accountNo)-4):
		if(accountNo[i]==accountNo[i+1] and accountNo[i]==accountNo[i+2] and accountNo[i]==accountNo[i+3]) :
			repeat=True
			break
	
	if repeat :
		print("Consecutive digits are repeating 4 or more times")	
	else :
		print("correct")	
else :
	print("wrong account number")
