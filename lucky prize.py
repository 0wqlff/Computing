#Ben lucky prize draw
import random
name1=input("Enter a name ")
name2=input("Enter a name ")
name3=input("Enter a name ")
name4=input("Enter a name ")
name5=input("Enter a name ")
name6=input("Enter a name ")
name7=input("Enter a name ")
name8=input("Enter a name ")
name9=input("Enter a name ")
name10=input("Enter a name ")
#the task of aquiring a number of names equal to ten has been officially completed
namelist=[name1,name2,name3,name4,name5,name6,name7,name8,name9,name10]
#names in array
prize=["a","b","c","d",]
numofnames=10
while (numofnames!=6):
    print(random.choice(namelist),"has won",random.choice(prize))
    numofnames=numofnames-1
