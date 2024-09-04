#Ben Wordle
secretword = ["z","e","b","r","a"]
guess = str(input("please enter your guess "))
guess= list(guess)
tries = 0
won = 0
while tries !=5:
    while (len(guess) !=5):
        guess = str(input("please enter a 5 letter word "))
        guess = list(guess)
        guess = str(input("please a enter a 5 letter word "))
    if (guess == secretword):
        print("You have guessed the correct word")
        won = 1
        
    if (won != 1):    
        if guess[0] in secretword:
            if (guess[0] == secretword[0]):
                print("The first letter of your guess is correct")
            else:
                print("The first letter of your guess is in the word but not that place")

        if guess[1] in secretword:
            if (guess[1] == secretword[1]):
                print("The second letter of your guess is correct")
            else:
                print("The second letter of your guess is in the word but not that place")

        if guess[2] in secretword:
            if (guess[2] == secretword[2]):
                print("The third letter of your guess is correct")
            else:
                print("The third letter of your guess is in the word but not that place")

        if guess[3] in secretword:
            if (guess[3] == secretword[3]):
                print("The fourth letter of your guess is correct")
            else:
                print("The fourth letter of your guess is in the word but not that place")

        if guess[4] in secretword:
            if (guess[4] == secretword[4]):
                print("The fourth letter of your guess is correct")
            else:
                print("The fourth letter of your guess is in the word but not that place")
        tries = tries + 1
            
    
    
