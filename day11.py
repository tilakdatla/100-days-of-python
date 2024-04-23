logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  elif sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

import random
def deal():
  cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
  return random.choice(cards)

def play_game():
  print(logo)
  user=[]
  computer=[]
  is_game_over=False
  for _ in range(2):
    user.append(deal())
    computer.append(deal())

  while not is_game_over:
    user_score=score(user)
    computer_score=score(computer)
    print("Your cards:",user,"current score:",user_score,"Computer's first card:",computer[0])
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("Type 'y' to get another card, type 'n' to pass:").lower()
      if user_should_deal=='y':
        user.append(deal())
      else:
        is_game_over=True


  while computer_score!=0 and computer_score<17:
    computer.append(deal())
    computer_score=score(computer)

  print("your score",user_score)
  print("computer score",computer_score)
  print(compare(user_score,computer_score))

while input("Do you want to play blackjack? type 'y' for yes and 'n' for no")=="y":
   play_game()


