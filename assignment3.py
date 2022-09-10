import random

max=int(input("Set a maximum number of this game: "))
min=1
target=random.randint(1,max)
while True :
	try :
		guess=int(input("Guess a number between "+str(min)+" and "+str(max)+" until you get it right : "))
	except:
		print("Please input a NUMBER between "+str(min)+" and "+str(max)+" !!!")
		continue
	if guess==target :
		print("BOOM !!!\nCongrats ! You have ended the game !")
		break
	elif guess==-1:
		print("esc")
		break;
	elif guess<=min :
		print("Please input a NUMBER between "+str(min)+" and "+str(max)+" !!!")
	elif guess>=max :
		print("Please input a NUMBER between "+str(min)+" and "+str(max)+" !!!")
	elif guess<target :
		min=guess
		print("Balloon is still being expanded…")
	elif guess>target :
		max=guess
		print("Balloon is still being expanded…")
	

	