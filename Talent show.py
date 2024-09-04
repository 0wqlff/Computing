#Ben
#Talent show
#computing
#25/6/24

name=str(input("What is your name? "))
age=int(input("How old are you? "))

while (age<11 or age>18):
    print("Invalid age")
    age=int(input("How old are you? "))

print("Welcome to the talent show",name)
