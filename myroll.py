#snake and ladder
import random
count=0
def roll():
	return random.randint(1,6)
while(count<=100):
	n=input("press r to roll the dive and q to quit the game")
	if(n=='r'):
		r=roll()
		count=count+r 
		print('u got',r) 
		print("new position is",count)
		if(count==8):
			count=37
			print("you got ladder,your current positions is",count)
		elif(count==11):
			count=2
			print("you have bitten by a snake,your current positions is",count)
		elif(count==13):
			count=34
			print("you got ladder,your current positions is",count)
		elif(count==25):
			count=4
			print("you have bitten by a snake,your current positions is",count)
		elif(count==38):
			count=9
			print("you have bitten by a snake,your current positions is",count)
		elif(count==40):
			count=68
			print("you got ladder,your current positions is",count)
		elif(count==52):
			count=81
			print("you got ladder,your current positions is",count)
		elif(count==65):
			count=46
			print("you have bitten by a snake,your current positions is",count)
		elif(count==76):
			count=97
			print("you got ladder,your current positions is",count)
		elif(count==89):
			count=70
			print("you have bitten by a snake,your current positions is",count)
		elif(count==93):
			count=64
			print("you have bitten by a snake,your current positions is",count)
		elif(count==100):
			print("you won the game")
			break
		if(count>100):
			count=count-r
			print("you cant go forword throw the dice again!")