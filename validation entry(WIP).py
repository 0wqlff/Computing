#Ben 21/9/23 Validation entry

done=0
print("""
Your choices are:
    1.crisps at 50p
    2.cans at 80p
    3.chocolate at 70p
    4.water at 40p
""")

while (done!=1):
    choice=input("Type 1,2,3 or 4 to choose ")
    if (choice==1):
        amount4=int(input("how many do you want? "))
        cost1= (amount4*50)
    if (choice==2):
        amount3=int(input("how many do you want? "))
        cost2= (amount3*80)
    if (choice==3):
        amount2=int(input("how many do you want? "))
        cost3= (amount2*70)
    if (choice==4):
        amount1=int(input("how many do you want? "))
        cost4= (amount1*40)
    yn=input("Are you done? ")
    if (yn=="yes"):
        done=1
    else:
        done=0
total=cost1+cost2+cost3+cost4
if (total<100):
    print("Please pay",total,"pence")
else:
    total=total/100
    print("Please pay",total,"pounds")
