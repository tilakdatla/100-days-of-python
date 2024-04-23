import random
print("Welcome to the PyPassword Generator!")
l=int(input("How many letters would you like in your password?\n"))
s=int(input("How many symbols would u like?\n"))
n=int(input("How many number would u like?\n"))

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=["1","2","3","4","5","6","7","8","0","9"]
symblos=['!','@','#','$','%','^','&','*','(',')']
password=""

for i in range(1,l+1):
    password+=random.choice(letter)

for i in range(1,s+1):
    password+=random.choice(symblos)

for i in range(1,n+1):
    password+=random.choice(numbers)

password2=""
for i in range(1,len(password)+1):
 password2+=random.choice(password)

print(password2)


























