#Ben
#Guess the number
#14/12/23
import random
number=(random.randint(0,10))
numofguess=1
guess=int
while (guess!=number):
    guess=int(input("input your guess "))
    if (guess!=number):
        print("wrong number try again")
    if (guess==number):
        print("Good job you found the number")
    elif (guess>number):
        print("The number is lower than your guess")
    elif (guess<number):
        print("The number is higher than you guess")
    if (guess<0 or guess>10):
        print("Please pick a number from 0-10")
        
    numofguess=numofguess+1
print("you got it in",numofguess,)
    
