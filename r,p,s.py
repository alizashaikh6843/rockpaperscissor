import random
print("welcome to rock paper sicssors game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock , paper, scissors]
user_choice = int(input("type 0 for rock 1 for paper and 2 for scissors\n"))
if user_choice < 0 or user_choice > 3:
  print("you have entered an invaid number, you lose")
else:
  print(game[user_choice])
    
  comp_choice = random.randint(0, 2)
  print("comuter's choice")
  print(game[comp_choice])
  
  if comp_choice == 2 and user_choice == 0:
    print("you win!")
  elif user_choice == 2 and comp_choice == 0:
    print("you lose!")
  elif user_choice > comp_choice:
    print("you win!")
  elif user_choice < comp_choice:
    print("you lose!")
  elif user_choice == comp_choice:
    print("it a draw!")
  else:
    print("you have entered a invalid number, you lose")
