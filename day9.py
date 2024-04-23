
'''
capitals={"france":"paris","germany":"berlin"}

travel_log=[
            {
                "country":"france",
                "cities_visited":["paris","lille",'dijon'],
                "total_visits":12
            },
            {
                "country":"germany",
                "citites_visited":["berlin","hamburg","stuttgart"],
                 "total_visits":5
            }
           ]

print(travel_log[0]['total_visits'])
'''


'''
print("Welcome to the secret auction program.")
dic = {}

while True:
    name = input("What is your name?:")
    price = int(input("What's your bid?$"))
    dic[name] = price
    n = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if (n == "yes"):
        clear()
    else:
        break

clear()
lis = []
for i in dic.values():
    lis.append(i)

for j in dic:
    if (max(lis) == dic[j]):
        print(f"The winner is {j} a bid of ${max(lis)}")
'''














