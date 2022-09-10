def add() :
	result=0;
	for i in range(len(series)-3, len(series)):
		result += series[i]
	return result

number = int(input("please enter a number: "))

series=[0,0,1]
tmp=0
while tmp<number :
	tmp=add()
	series.append(tmp)

if tmp==number :
	print("true")
else :
	print("false")


