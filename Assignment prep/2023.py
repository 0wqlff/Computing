start_mileage = int(input("Enter the vehicle mileage at the start of the journey: "))
no_chargingstations = int(input("Enter the number of charging stations visited during the journey: "))
total_cost=0
journeyscost=[]
total_miles=0



for i in range(no_chargingstations):
    kwrating = int(input("Enter the kilowatt rating at charging station number",(i+1),": "))
    chargemileage=int(input("Enter the vehicle mileage at charging station number",(i+1),": "))
    while (kwrating != 7 and kwrating != 22 and kwrating != 50):
        print ("ERROR - invalid kilowatt rating")
        kwrating = int(input("Enter the kilowatt rating for this charging station: "))
    milesTravelled=chargemileage-start_mileage
    total_miles+=milesTravelled
    start_mileage=chargemileage
    if (kwrating==7):
        cost=0*milesTravelled
    elif(kwrating==22):
        cost=0.005*milesTravelled
    else:
        cost=0.01*milesTravelled
    total_cost+=cost
    journeyscost.append(cost)

print("The total cost of the journey was",round(total_cost,2),"pounds")
print("The total miles travelled in the journey was",total_miles,"miles")
for i in range(no_chargingstations):
    print("The cost for stage",i+1,"of the journey was",round(journeyscost[i],2),"pounds")



