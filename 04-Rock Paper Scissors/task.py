import  random
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

rock_paper_scissor_list = [rock , paper , scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(rock_paper_scissor_list[user_choice])

print(f"Computer chose:\n{rock_paper_scissor_list[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == computer_choice:
    print("Draw!")
else:
    print("You Lose!")