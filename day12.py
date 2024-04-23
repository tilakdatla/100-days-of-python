# local and global variable
logo="""  _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                  """
import random
numbers = list(range(1, 101))
number=random.choice(numbers)
print(number)
print(logo)
print("welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100")
choice=input("choose a difficulty type 'easy' or 'hand'").lower()


if choice=="easy":
    attempt=10
    while attempt!=0:
        print(f"You have {attempt} to guess the number")
        n=int(input("Make a guess"))
        if(n==number):
            print("you win")
            break
        elif n<number:
            print("Too low")
        else:
            print("Too high")
        attempt-=1
    if attempt==0:
        print("you lose,run out of attempts")
elif choice=="hard":
    attempt=5
    while attempt!=0:
        print(f"You have {attempt} to guess the number")
        n=int(input("Make a guess"))
        if(n==number):
            print("you win")
            break
        elif n<number:
            print("Too low")
        else:
            print("Too high")
        attempt-=1
    if attempt==0:
        print("you lose,run out of attempts")

else:
    print("enter a valide choice")












