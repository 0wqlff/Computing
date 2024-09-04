#Ben
#9/1/24
#Getting to know you

#firstname = str(input("What is your first name? "))
#lastname = str(input("What is your last name? "))
#age = int(input("How old are you? "))
#enjoy = input("Do you enjoy programming? y/n? ")
#books = []
#book1 = input("What was the last book you read? ")
#book2 = input("What was the second last book you read? ")
#book3 = input("What was the third last book you read? ")
#books.append(book1)
#books.append(book2)
#books.append(book3)
#print("Your name is",firstname,lastname)
#print("You are",age,"years old")
#if (enjoy=="y"):
#    print ("You enjoy programming")
#else:
#    print ("You do not enjoy programming")

#print("the last 3 books you read were",books)

numbers = [45,75,23,54,76,23]
total = 0
for i in range(6):
    total = total+numbers[i-1]
    i = i+1

print ("the total of the numbers is",total)
