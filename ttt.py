import random
a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print('\n -----')
	print( '|' + a[0] +'|' + a[1] + '|' + a[2] + '|' )
	print('-----')
	print( '|' + a[3] +'|' + a[4] + '|' + a[5] + '|' )
	print('-----')
	print( '|' + a[6] +'|' + a[7] + '|' + a[8] + '|' )

p1=True

while(True):
	printboard()
	#player 1 plays

	if p1:
		p=input("player 1, choose ur place : ")
		if p in a:
			a[int(p)-1]='X'
			p1 =not p1
		else:
			p=input("player 2, choose ur place : ")
			if p in a:
				a[int(p)-1]='o'
				p1 =not p1

#check each columns
for i in range(3):
	if(a[i]==a[i+1] and a[i]==a[i+2]):
		print("game over")
		printboard()
		exit()


#check each row
for i in(0,3,6):
	if(a[i]==a[i+3] and a[i]==a[i+6]):
		print("game over")
		printboard()
		exit()
 
 #check each diagonal from left to right 
    if(a[i]==a[i+4] and a[i]==a[i+8]):
    	print("game over")
    	printboard()
    	exit()

#check each diagonal from right to left 
    if(a[2]==a[4] and a[2]==a[6]):
    	print("game over")
    	printboard()
    	exit()
