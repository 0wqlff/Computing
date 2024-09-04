travel_agent = []
booking_number = []
dates = []
for index in range(3):
    travelagent = input(" Enter travel agent ")
    bookingnumber = int(input(" Enter your booking number "))
    date = input(" Enter your date of travel ")
    travel_agent.append(travelagent)
    booking_number.append(bookingnumber)
    dates.append(date)
print(travel_agent)
print(booking_number)
print(dates)