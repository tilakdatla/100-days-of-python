print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

n=input('''You'r at a cross road. where do you want to go? Type "left" or "right"\n''')

if(n=="left"):
 w=input('You come to a lake, There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n')
 if(w=="wait"):
     c=input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which color do you choose?\n")
     if(c=="blue"):
         print("You enter a room of beasts. Game Over.")
         print("This repl has exited, run again?")
     elif(c=="red"):
         print("You enter a room of beasts. Game Over.")
         print("This repl has exited, run again?")
     elif(c=="yellow"):
         print("congrates u found the treasur")
     else:
         print("Invalide choice")
 if(w=="swim"):
     print("Game over")
else:
    print("Game over")


