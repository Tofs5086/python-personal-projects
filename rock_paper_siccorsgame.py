import random
user_choice=int(input('enter your choice: type 0 for rock, 1 for paper, 2 for scissors')) #takes input from the user
if user_choice > 2 or user_choice < 0:  #1st condition
    print('you entered an invalid number boss, you lose, ha ha ha')
else:
    computer_choice = random.randint(0, 2)
    print('computer chose:')
    print(computer_choice)
    if computer_choice == user_choice: #2nd condition
        print("it's a draw")
    elif computer_choice == 0 and user_choice == 2:
        print('you lose')
    elif user_choice == 0 and computer_choice == 2:
        print('you win')
    elif computer_choice > user_choice: #3rd conndition
        print('you lose')
    elif user_choice > computer_choice:
        print('you win')
