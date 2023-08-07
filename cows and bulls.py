import random
while True:
    print('--------------------------------------------------------------------------------')
    print('~Game: Cows & Bulls~')
    easy=['rat','cat','pen','bat','van','rug','mug']
    medium=['boat','leaf','ride','game','goat','rock','beat']
    hard=['paper','right','wrong','clock','guess','maths','towel']
    d=random.randrange(0,7)
    print("Please choose your level(1/2/3)","\n1.Easy\n2.Medium\n3.Hard")
    n=int(input('Enter your choice:'))
    
    while n>3 or n<1:
        n=int(input('Enter a valid choice:'))
        
    if n==1:
        word=easy[d]
        guesses=4
        size=3
    elif n==2:
        word=medium[d]
        guesses=9
        size=4
    else:
        word=hard[d]
        guesses=14
        size=5
    print('--------------------------------------------------------------------------------')
    print("Guess the word. It contains" ,size, "letters.")

    remaining_turns = guesses

    while remaining_turns <= guesses:

        player_guess=input('Please enter your guess:')
        if len(player_guess) != size:
            print("Your guess must have", size,"letters only.")
            continue


        if player_guess == word:
            print("Yay, you guessed it rigt!")
            break
        
        else:
            bulls = 0
            cows = 0
            
            for i in range(size):
                if player_guess[i] == word[i]:
                    bulls += 1
                    
            for j in range(size):
                if player_guess[j] in word and \
                  player_guess[j] != word[j]:
                    cows += 1
                    
            print("Bulls: ",bulls)
            print("Cows: ",cows)
            print('You have',remaining_turns,'turns remaining.')
            print('--------------------------------------------------------------------------------')
            
            remaining_turns -= 1
            
            if remaining_turns < 0:
                print("You lost the game.")
                print('The word is..',word)
                break
    print('Do you want to try again? (y/n)')
    c=input()
    if c =='n' or c=='N':
        print('Thanks for playing')
        print('--------------------------------------------------------------------------------')
        break
            
