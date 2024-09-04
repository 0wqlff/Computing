#Grade Award
#Ben
#28/9/23

name=input("Please enter your name ")
mark=int(input("Please enter your mark "))
if (mark>69 and mark<101):
    print(name,"got",mark,"percent and was awarded an A")
elif (mark>60 and mark<69):
    print(name,"got",mark,"percent and was awarded a B")
elif (mark>50 and mark<59):
    print(name,"got",mark,"percent and was awarded a C")
elif (mark>40 and mark<49):
    print(name,"got",mark,"percent and was awarded a D")
elif (mark>0 and mark<39):
    print(name,"got",mark,"percent and was awarded an F")
else:
    print("Invalid entry please try again")
