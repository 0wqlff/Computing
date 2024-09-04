#Ben
#Tuckshop
#14.9.23
done=0
print("""
Your choices are:
    1.crisps at 50p
    2.cans at 80p
    3.chocolate at 70p
    4.water at 40p
""")

while (done!=1):
    choice=int(input("Type 1,2,3 or 4 to choose "))
    if (choice==1):
        amount=int(input("how many do you want? "))
        cost = (amount*50)
    elif (choice==2):
        amount=int(input("how many do you want? "))
        cost = (amount*80)         
    elif (choice==3):
        amount=int(input("how many do you want? "))
        cost = (amount*70)
    elif (choice==4):
        amount=int(input("how many do you want? "))
        cost = (amount*40)
    else:
        print("Invalid Entry Please try again")
    yn=input("Are you done? ")
    if (yn=="yes"):
        done=1
    else:
        done=0

if (cost<100):
    print("Please pay",cost,"pence")
else:
    cost=cost/100
    print("Please pay",cost,"pounds")
    
    
