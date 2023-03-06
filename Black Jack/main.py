
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

import random
cards = ["11", " 2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
user_random = []
computer_random=[]
def initial_card():
    initial_1 = random.choice(cards)
    user_random.append(initial_1)
    initial_2 = random.choice(cards)
    user_random.append(initial_2)
    score = int(initial_1) + int(initial_2)
    if(score==22):
      user_random.remove("11")
      user_random.append("1")
    print(f"your card is:{user_random} current value:{score}")
def initial_computer():
    initial_1 = random.choice(cards)
    computer_random.append(initial_1)
    initial_2 = random.choice(cards)
    computer_random.append(initial_2)
    score=int(initial_1)+int(initial_2)
    if(score==22):
      computer_random.remove("11")
      computer_random.append("1")
    print(f"computer first card [{computer_random[0]}]")    
def selection():
    return random.choice(cards)
print(logo)
x = input("do you want to play the game blackjack 'y'to continue and n to exit")
while(x=="y"):
  final_computer_total=0
  final_user_total=0
  if (x == "y" ):
    initial_card()
    initial_computer()
    total=0
    for i in user_random:
        total+=int(i)  
    user_choose=input("if you want another card type 'y' or you want to pass type 'n'")
    user_choose_1=user_choose

    if(total<=21 and user_choose_1=="y"):
      while(user_choose_1=="y" and total<=21):
    
        z=selection()
        user_random.append(z)
        total_1=0
        for num in user_random:
          total_1+=int(num)
        if(z=="11" and total_1<=21):  
          total=total_1
        elif(z=="11" and total_1>21):
          total_1-=10
          user_random.remove("11")
          user_random.append("1")
          total=total_1
        else:
          total=total_1  

        print(f"your final hand{user_random} and total score{total_1}")
        final_user_total=total_1
        if(total<=21 and user_choose_1=="y"):
          user_choose_2=input("if you want another card type 'y' or you want to pass type 'n'")
       
          user_choose_1=user_choose_2
 
    else:
      final_user_total=total            
  
  if(user_choose=="n" or user_choose_1=="n"):

      total=0
      for i in computer_random:
        total+=int(i)
      while(total<21):
       choose=["y","n"]
       another_card = random.choice(choose)
       if(another_card=="y"):
          while(total<21):  
            f=selection()
            computer_random.append(f)
            total=0
            for num in computer_random:
              num_1=int(num)
              total+=num_1
            if(f=="11" and total<=21):  
               total=total
            elif(f=="11" and total>21):
               total-=10
               computer_random.remove("11")
               computer_random.append("1")
            else:
               total=total  
          print(f"computer's final hand:{computer_random} final score:{total}")
          final_computer_total=total
       else:
          print(f"computer's final hand:{computer_random} final score:{total}")
          final_computer_total=total
          break
  else:
      print("brust😳")
      print("you lose😭")
      x = input("do you want to play the game blackjack 'y'to continue and n to exit")
      if(x=="y"):
    
       user_random = []
       computer_random=[]
           
  if(final_user_total==final_computer_total):
    print("draw😜")
    x = input("do you want to play the game blackjack 'y'to continue and n to exit")
    if(x=="y"):
       
       user_random = []
       computer_random=[]
       
  elif(final_user_total> final_computer_total and final_user_total<=21):
    print("you win🥳")
    x = input("do you want to play the game blackjack 'y'to continue and n to exit")
    if(x=="y"):

       user_random = []
       computer_random=[]
       
  elif(final_computer_total>final_user_total and final_computer_total>21):
    print("you win🥳")
    x = input("do you want to play the game blackjack 'y'to continue and n to exit")
    if(x=="y"):
       
       user_random = []
       computer_random=[]
         
  elif(final_computer_total>final_user_total and final_computer_total<=21):
    print("you lose😭")
    x = input("do you want to play the game blackjack 'y'to continue and n to exit")
    if(x=="y"):
       
       user_random = []
       computer_random=[]
       
