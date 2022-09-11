import random

# ask user input max range and store in variable max
max=int(input("Set a maximum number of this game: "))

# default min value as 1
min=1

#set target
target=random.randint(min+1,max-1)

#loop
while True :
	
	# try catch block
	try :

		# ask user input a number between min and max , then convert the input to int
		guess=int(input("Guess a number between "+str(min)+" and "+str(max)+" until you get it right : "))

	#catch exception if user input non int value which cannot be convert to int
	except:
		print("Please input a NUMBER between "+str(min)+" and "+str(max)+" !!!")
		# skip all the following code
		continue

	# check if the input match the target
	if guess==target :
		print("BOOM !!!\nCongrats ! You have ended the game !")

		# break the loop
		break

	# escape point, input -1 if u dont want to finish the game
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