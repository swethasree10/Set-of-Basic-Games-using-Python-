import random
user_count=comp_count=0
print('--------------------------------------------------------------------------------')
print('Game:Rock,Paper,Scissors \nGAME RULES \nRock VS Paper ~ PAPER wins \nPaper VS Scissors ⟶ SCISSORS wins \nScissors VS Rock ⟶ ROCK wins')
print('--------------------------------------------------------------------------------')
while True: 
	print("1. ROCK \n2. PAPER \n3. SCISSORS") 
	choice = int(input("WHAT'S YOUR CHOISE(1/2/3)? "))
	while choice > 3 or choice < 1: 
		choice = int(input("Enter a Valid Choise!! ")) 
	if choice == 1: 
		choice_name = 'ROCK'
	elif choice == 2: 
		choice_name = 'PAPER'
	else: 
		choice_name = 'SCISSORS'
		
	
	print("\nYour Choise is ⟶ ",choice_name) 
	print("\nNow it's the Computers Turn... ") 


	comp_choice = random.randint(1, 3) 
	
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	if comp_choice == 1: 
		comp_choice_name = 'ROCK'
	elif comp_choice == 2: 
		comp_choice_name = 'PAPER'
	else: 
		comp_choice_name = 'SCISSORS'
		
	print("The Computers Choise is ⟶ ",comp_choice_name,'\n') 

		
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):  
		result = "PAPER"
		
	elif((choice == 1 and comp_choice == 3) or
	(choice == 3 and comp_choice == 1)): 

		 result = "ROCK"
	else: 
		 
		result = "SCISSORS"

	
	if result == choice_name: 
		print("YAY! YOU WIN :) ")
		print('--------------------------------------------------------------------------------')
		user_count+=1
	else: 
		print("OOPS! THE COMPUTER WINS :( ")
		print('--------------------------------------------------------------------------------')
		comp_count+=1
		
	print("WANNA TRY AGAIN(Y/N)? ",end='')
	ans = input()
	print('--------------------------------------------------------------------------------')
	if ans == 'n' or ans == 'N':
		break
	
print('\tSCORE BOARD \n     Your Points:',user_count,'\n     Computers Points:',comp_count)
if user_count>comp_count:
        print('\nCONGRAGULATIONS!! YOU HAVE WON THIS GAME :)')
elif comp_count>user_count:
        print('\nHARD LUCK THE COMPUTER WON :(')
else:
        print('\nIT IS A TIE')

print("Thanks for playing come back soon :)")
print('--------------------------------------------------------------------------------')



























































