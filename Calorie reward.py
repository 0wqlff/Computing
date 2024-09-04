#Ben
#5/9/23
#Calorie reward
Breakfast=int(input("How many calories were in you breakfast? "))
lunch=int(input("How many calories were in you lunch? "))
Dinner=int(input("How many calories were in you dinner? "))
total=Breakfast+lunch+Dinner
burnt=int(input("How many calories have you burnt today? "))
print("You have consumed",total,"calories today")
netloss=burnt-total
if (netloss>0):
    print("You have lost",netloss,"calories")
if (netloss>100):
      print("You get a treat today for losing more than 100 calories!!!!")
if (netloss<0):
    netloss=netloss*-1
    print("You have gained",netloss,"calories today")
