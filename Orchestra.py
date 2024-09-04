#Orchestra
#Ben
#7/12/23
noOfaplicants=5
names=[]
junior=[]
senior=[]
denied=[]
for i in range(0,noOfaplicants):
    name=str(input("What is your name? "))
    names.append(name)
    age=int(input("How old are you? "))
    test1=int(input("What score did you get for test 1? "))
    test2=int(input("What score did you get for test 2? "))
    if (age>11 and age<15 and test1+test2>69):
        junior.append(name)
    elif (age>14 and age<18 and test1+test2>69):
        senior.append(name)
    else:
        denied.append(name)
    
        

print(junior,"all made it into the junior orchestra")
print(senior,"all made it into the senior orchestra")
print(denied,"did not meet the requirements")



    
    
