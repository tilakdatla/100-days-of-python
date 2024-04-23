#string

'''
print("hello"[-1])
print(len("123"))
'''

#float
'''
print(3.14)
'''
'''
print(3*3+3/3-3)
print(3*(3+3)/3-3)
'''
'''
print(round(2.666666666,2))
'''

#f-string
'''
score=0
height=1.54
iswinning=True
print(f"your score is {score}, your hieght is {height}, you are winning is {iswinning}")
'''



print("Welcome to the tip calculator")
n=float(input("What was the total bill?$"))
p=int(input("What percentage tip would you like to give?10, 12, or 15?"))
person=int(input("How many to split the bill? "))
s=0
if(p==10):
    s=n+(n*0.1)
elif(p==12):
    s=n+(n*0.12)
elif(p==15):
    s=n+(n*0.15)
else:
    print("enter other value")

round(s/person,2)
print("Each person should pay:",round(s/person,2))
