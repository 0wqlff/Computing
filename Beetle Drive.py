#Ben
#Beetle drive
#16/11/23
import turtle
import random
from turtle import Screen, Turtle
s = turtle.getscreen()
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
dice = (random.randint(1,6))
six="y"
five="y"
two="y"
on=0
counttwo=int(1)
countfour=int(1)
countthree=int(1)
countone=int(1)
t5.ht()
t.ht()
t2.ht()
t3.ht()
t4.ht()
while (on!=1):
    while (six=="y"):
        dice = (random.randint(1,6))
        if (dice==6):
            print("You have rolled a 6, you have a body")
            t.ht()
            t.lt(90)
            t.fd(100)
            t.lt(90)
            t.fd(80)
            t.lt(90)
            t.fd(100)
            t.lt(90)
            t.fd(80)
            six="n"
            #roll for 6
            while (five=="y"):
                dice = (random.randint(1,6))
                if (dice==5):
                    print("You have rolled a 5, you have a head")
                    t.ht()
                    t.lt(90)
                    t.fd(100)
                    t.lt(90)
                    t.fd(20)
                    t.rt(90)
                    t.fd(40)
                    t.lt(90)
                    t.fd(40)
                    t.lt(90)
                    t.fd(40)
                    five="n"
                    #roll for 5 if you have 6
                    while (two=="y"):
                        dice = (random.randint(1,6))
                        if (dice==2):
                            if (counttwo==1):
                                print("You have rolled a 2, you have the first feeler")
                                t.ht()
                                t.lt(180)
                                t.fd(40)
                                t.lt(90)
                                t.fd(5)
                                t.rt(90)
                                t.fd(20)
                                t.lt(90)
                                t.fd(20)
                                t.rt(90)
                                t.fd(20)
                                two="n"
                                counttwo=counttwo+1
                                two="y"
                                dice = (random.randint(1,6))
                        if (dice==2):
                            if (counttwo==2):
                                print("You have rolled another 2, you have the second feeler")
                                t.ht()
                                t.lt(180)
                                t.up()
                                t.goto(-20,140)
                                t.down()
                                t.lt(90)
                                t.fd(5)
                                t.lt(90) 
                                t.fd(20)
                                t.rt(90)
                                t.fd(20)
                                t.lt(90)
                                t.fd(20)
                                two="n"
                                if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                                    six="N"
                                    five="n"
                                    two="n"
                                    on=1
                                    print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                            counttwo=counttwo+1
    
                        if (dice==4):
                            if (countfour==1):
                                print("You have rolled a 4 you now have the tail")
                                t2.ht()
                                t2.bk(40)
                                t2.rt(90)
                                t2.fd(40)
                                countfour=countfour+1
                        if (dice==3):
                            if (countthree==1):
                                print("You have rolled a 3 you have your first leg")
                                t3.ht()
                                t3.lt(90)
                                t3.fd(25)
                                t3.rt(90)
                                t3.fd(20)
                                dice = (random.randint(1,6))
                                countthree=countthree+1
                        if (dice==3):
                            if (countthree==2):
                                print("You have rolled a 3 you have your second leg")
                                t3.bk(20)
                                t3.lt(90)
                                t3.fd(25)
                                t3.rt(90)
                                t3.fd(20)
                                countthree=countthree+1
                                dice = (random.randint(1,6))
                        if (dice==3):
                            if (countthree==3):
                                print("You have rolled a 3 you have your third leg")
                                t3.bk(20)
                                t3.lt(90)
                                t3.fd(25)
                                t3.rt(90)
                                t3.fd(20)
                                countthree=countthree+1
                                dice = (random.randint(1,6))
                        if (dice==3):
                            if (countthree==4):
                                print("You have rolled a 3 you have you fourth leg")
                                t4.lt(180)
                                t4.fd(80)
                                t4.rt(90)
                                t4.fd(25)
                                t4.lt(90)
                                t4.fd(20)
                                countthree=countthree+1
                                dice = (random.randint(1,6))
                        if (dice==3):
                            if (countthree==5):
                                print("You have rolled a 3 you have you fifth leg")
                                t4.bk(20)
                                t4.rt(90)
                                t4.fd(25)
                                t4.lt(90)
                                t4.fd(20)
                                countthree=countthree+1
                                dice = (random.randint(1,6))
                        if (dice==3):
                            if (countthree==6):
                                print("You have rolled a 3 you have you sixth leg")
                                t4.bk(20)
                                t4.rt(90)
                                t4.fd(25)
                                t4.lt(90)
                                t4.fd(20)
                                countthree=countthree+1
                                if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                                    six="N"
                                    five="n"
                                    two="n"
                                    on=1
                                    print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                                else:
                                    dice = (random.randint(1,6))
                        if (dice==1):
                            if (countone==1):
                                print("You have rolled a 1 you have your first eye")
                                t5.up()
                                t5.goto(-50,120)
                                t5.down()
                                t5.fd(4)
                                countone=countone+1
                                dice = (random.randint(1,6))
                        if (dice==1):
                            if (countone==2):
                                print("You have rolled a 1 you have your second eye")
                                t5.up()
                                t5.goto(-30,120)
                                t5.down()
                                t5.fd(4)
                                countone=countone+1
                                if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                                    six="N"
                                    five="n"
                                    two="n"
                                    on=1
                                    print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                                else:
                                    dice = (random.randint(1,6))
                        else:
                            print("you have rolled a ",dice,)
                            two = input("You didnt roll anything useful do you want to roll again(y/n)")
                            if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                                    six="N"
                                    five="n"
                                    two="n"
                                    on=1
                                    print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                        

             

                if (dice==4):
                    if (countfour==1):
                        print("You have rolled a 4 you now have the tail")
                        t2.ht()
                        t2.bk(40)
                        t2.rt(90)
                        t2.fd(40)
                        countfour=countfour+1
                        if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                            six="N"
                            five="n"
                            on=1
                            print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                if (dice==3):
                    if (countthree==1):
                        print("You have rolled a 3 you have your first leg")
                        t3.ht()
                        t3.lt(90)
                        t3.fd(25)
                        t3.rt(90)
                        t3.fd(20)
                        countthree=countthree+1
                        dice = (random.randint(1,6))
                if (dice==3):
                    if (countthree==2):
                        print("You have rolled a 3 you have your second leg")
                        t3.bk(20)
                        t3.lt(90)
                        t3.fd(25)
                        t3.rt(90)
                        t3.fd(20)
                        countthree=countthree+1
                        dice = (random.randint(1,6))
                    
                if (dice==3):
                    if (countthree==3):
                        print("You have rolled a 3 you have your third leg")
                        t3.bk(20)
                        t3.lt(90)
                        t3.fd(25)
                        t3.rt(90)
                        t3.fd(20)
                        countthree=countthree+1
                        dice = (random.randint(1,6))
                if (dice==3):
                    if (countthree==4):
                        print("You have rolled a 3 you have your fourth leg")
                        t4.lt(180)
                        t4.fd(80)
                        t4.rt(90)
                        t4.fd(25)
                        t4.lt(90)
                        t4.fd(20)
                        countthree=countthree+1
                        dice = (random.randint(1,6))
                if (dice==3):
                    if (countthree==5):
                        print("You have rolled a 3 you have your fifth leg")
                        t4.bk(20)
                        t4.rt(90)
                        t4.fd(25)
                        t4.lt(90)
                        t4.fd(20)
                        countthree=countthree+1
                        dice = (random.randint(1,6))
                if (dice==3):
                    if (countthree==6):
                        print("You have rolled a 3 you have your sixth leg")
                        t4.bk(20)
                        t4.rt(90)
                        t4.fd(25)
                        t4.lt(90)
                        t4.fd(20)
                        countthree=countthree+1
                        if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                            six="N"
                            five="n"
                            two="n"
                            on=1
                            print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                        else:
                            dice = (random.randint(1,6))
                        
                else:
                    print("you have rolled a",dice,)
                    five = input("You didnt roll anything useful do you want to roll again(y/n)")
                    if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                        print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
                        six="n"
                        five="n"
                        two="n"
                        on=1
        else:
            print("you have rolled a",dice,)
            six = input("You didnt roll a 6 do you want to roll again(y/n)")
            if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
                six="N"
                five="n"
                on=1
                print("You have won!!!!!!! wooohoo")
    if (countthree>6 and counttwo>2 and countfour>1 and countone>2):
        print("You have won!!!!!!! wooohoo (i tried to code it to end by itself but it was already BUGGY enough)")
        six="n"
        five="n"
        two="n"
        on=1
