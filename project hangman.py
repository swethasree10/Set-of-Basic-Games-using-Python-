import random
while True:
    name=input("Enter your name :")
    print("Good Luck!",name,"\nPlease choose your level(1 or 2 or 3)","\n1.Easy\n2.Medium\n3.Hard")
    n=int(input("Enter your choice:"))

    d=random.randrange(0,20)

    words1=['burn','happy','songs','jelly','flower','godess','frank','logic','hate','basic','draw','tooth','books','paper','range','smile','blog','notes','dance','game']

    words2=['masculine','irregular','challenge','australia','dangerous','wrestling','undefined','ambulance','thursday','fourteen','sensible','drooping','ordinary','construct','president','delecious','xylophone','amendment','magnesium','carribean']

    words3=['procrastination','personification','characteristics','desertification','rumpelstiltskin','abdominovesical','alphabetisation','influentialness','pulchritudinous','thermochemistry','discrimination','photosynthesis','constantinople','saponification','transformation','multiplication','capitalization','transportation','trichomoniasis','responsibility']

    if n==1:
        word=words1[d]
        turns=6
    elif n==2:
        word=words2[d]
        turns=9
    elif n==3:
        word=words3[d]
        turns=15 
    else:
        print('invalid input')
    print('Start guessing the letters now :')
    guesses=''
    while turns>0:
        failed=0
        for char in word:
            if char in guesses:
                print(char,end=' ')
            else:
                print("_", end=' ')
                failed+=1
        if failed==0:
                print("\nCongradulations!",name, "You Won ^_^")
                print("The word is",word)
                break
        guess=input("\nGuess a letter:")
        guesses+=guess
        if guess not in word:
            turns-=1
            print("Oops! Wrong guess :/")
            print("You have",turns,"more guesses left")
            if turns==0:
                print("You loose :/ Better luck next time ")

    print("WANNA TRY AGAIN? (Y/N)") 
    ans = input() 
    if ans == 'n' or ans == 'N':
        print('THANKS FOR PLAYING')
        break      

























                
