#Ben
#7/9/23
#Net calories gained
calories_burned = [0,0,0,0,0,0,0]
calories_consumed = [0,0,0,0,0,0,0]
chosen = [False,False,False,False,False,False,False,]
total = 0
net_gain = [0,0,0,0,0,0,0]

for day in range(7):
    print("Day", day + 1)
    calories_consumed[day] = int(input("How many calories did you consume? "))
    calories_burned[day] = int(input("How many calories did you burn? "))
    net_gain[day] = calories_consumed[day] - calories_burned[day]
for day in range(7):
    print(day + 1,"\t\t",
          calories_consumed[day],"\t\t\t",
          calories_burned[day],"\t\t", net_gain[day])
total = total + net_gain[day]
for day in range(7):
    answer = input("Enter y to display day  " +str(day+1))
    if (answer == "y"):
        chosen[day] = True

print("Day \t calories consumed \t calories burnt \t net gain")
for day in range(7):
    if chosen[day] == True:
        print(day+1,"\t\t",calories_consumed[day],"\t\t\t",
              calories_burned[day],"\t\t",net_gain[day])
        total = total + net_gain[day]

                
print("that comes to",total," calories")
