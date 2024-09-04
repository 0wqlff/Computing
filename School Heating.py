#Ben
#school heating
#16/11/23
ArtTemp=int(input("Please enter the temperature in Art "))
EngTemp=int(input("Please enter the temperature in English "))
MusicTemp=int(input("Please enter the temperature in Music "))
AvgTemp=(ArtTemp+EngTemp+MusicTemp)/3
print("the average temperature is",AvgTemp,)
if (AvgTemp<17):
    print("The Heating should be on")
else:
    print("The Heating should be off")
