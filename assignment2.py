# define a function call "add"
def add() :
	# init result
	result=0;

	# array index starts from 0; in the first round of the loop, array series only have 3 items, len(series)-3 = 0, len(series) = 3; the loop will loop from 0-2
	for i in range(len(series)-3, len(series)):
		result += series[i]
	
	return result

# ask user input an int and assign the inputed int to number
number = int(input("please enter a number: "))

series=[0,0,1]
tmp=0

while tmp<number :
	# call "add" function and asign the retuned value to tmp
	tmp=add()
	# add tmp to array series
	series.append(tmp)

if tmp==number :
	print("true")
else :
	print("false")


