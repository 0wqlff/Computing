Childbuffet = 2
cakereq = input("is cake required Y/N? ")
if (cakereq == "Y"):
    cake = 15
else:
    cake = 0
NOofchildren=int(input("How many children are there? "))
NOofadults=int(input("How many adults are there? "))
dietreq=[]
for index in range(NOofchildren):
    msg="Are there any dietary requirements for child",index+1
    reqs=input(msg)
    dietreq.append(reqs)
if (NOofadults+NOofchildren)<20:
    venue=0
else:
    venue=50
cost=Childbuffet*NOofchildren+cake+venue
print("The total cost will be £",cost)
