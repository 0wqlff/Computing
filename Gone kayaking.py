#Ben
#Gone Kayaking
#14/12/23
kayakhired=int(input("How many kayaks do you wish to hire? "))
kayakcost=kayakhired*25
instructorHire=str(input("Do you want an instructor? (y/n) "))
totalcost=kayakcost
if (kayakhired>20):
    print("sorry we only have 20 kayaks")
if (instructorHire=="y"):
    totalcost=totalcost+80
print("Please pay ",totalcost,"pounds")
