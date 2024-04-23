'''
def greet(name,location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
greet(location="gaduli",name="tilak",)
'''


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
def encrypt(text, shift):
    output = ""
    for i in text:
      if i in li:
        n = li.index(i)
        output += li[n + shift]
      else:
          output+=i
    print(output)

def decrypt(text,shift):
    output = ""
    for i in text:
      if i in li:
        n = li.index(i)
        output += li[n - shift]
      else:
          output += i
    print(output)
while True:
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt and exit for end\n").lower()
    if direction == "exit":
        break
    elif direction=="encode":
        text = input("Type your msg\n").lower()
        shift = int(input("Type the shift number:\n"))%26
        encrypt(text, shift)
    elif direction=="decode":
        text = input("Type your msg\n").lower()
        shift = int(input("Type the shift number:\n"))%26
        decrypt(text, shift)
    else:
        print("enter valide input")






