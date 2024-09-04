#Ben
#5/9/23
#Garden Centre

tulips_spend=int(input("How many pounds did you spend on tuplips? "))
crocuses_spend=int(input("How many pounds did you spend on crocuses? "))
snowdrops_spend=int(input("How many pounds did you spend on snowdrops? "))
daffodils_spend=int(input("How pounds did you spend on daffodils? "))
total_spend=tulips_spend+crocuses_spend+snowdrops_spend+daffodils_spend
print("You have spent" ,total_spend, "pounds")
if (total_spend>30):
    print("You get a free hyacinth since you spent more than £30")
