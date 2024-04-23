'''
import random
random_int=random.random()
print(random_int*5)

import random

random_int=random.randint(0,1)

if(random_int<=0):
    print("Heads")
else:
    print("Tails")
'''

'''
names=[eval(a) for a in input("enter name ").split(",")]
import random

name=names[random.randint(0,len(names))]
print(name,"is going to buy the meal today!")
'''

'''
name=["tilak","ronak","jainil","arpit"]
game=["cricket","football","kabaddi"]

all=[name,game] #nested list
print(all[1][1])
'''

'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

r=(position%10)-1
position=(position//10)-1

map[r][position]="x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
'''





























