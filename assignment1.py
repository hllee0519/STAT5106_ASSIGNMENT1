import re
def checkAccNo(accountNo) :
	# create regular expression
	regexWithHyphen = re.compile("^[4|5|6][0-9]{3,3}-[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}$")
	regexWithoutHyphen=re.compile("^[4|5|6][0-9]{15,15}$")
	# compare the inputed acc no to the regex
	if regexWithHyphen.match(accountNo) or regexWithoutHyphen.match(accountNo) :

		# remove '-' if any
		accountNo=accountNo.replace('-', '')


		#  for check consecutive digits repeating 4 or more times
		for i in range(0, len(accountNo)-4):
			if(accountNo[i]==accountNo[i+1] and accountNo[i]==accountNo[i+2] and accountNo[i]==accountNo[i+3]) :
				return False
		return True
	else:
		return False




# ask user input account number
accountNo=input("Please enter your account number: ")

if checkAccNo(accountNo) :
	print("Valid")
else : 
	print("Invalid")
	
	
