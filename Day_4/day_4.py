import random
print("Welcome to Rock, Paper, Scissors Shoot!")
computer_choice = (random.choice([0, 1 , 2]))
begin = input ("Would you like to play y or n? ")
if begin == "n":
    print("Bro why are you here?")
elif begin == "y":    
    print("Let's begin!")
user_choice = int(input("What do you choose? For Rock type 0, for Paper type 1, for Scissors, type 2 "))

if user_choice == 0 and computer_choice == 2:
    print("You win, rock beats scissors.")
elif user_choice == 2 and computer_choice == 1:
    print("You win, scissors beats rock.")
elif user_choice == 1 and computer_choice == 0:
    print("You win, paper beats rock")
elif computer_choice == 0 and user_choice == 2:
    print("You lost, rock beats scissors")
elif computer_choice == 2 and user_choice == 1:
    print("You lost, scissors beats paper")
elif computer_choice == 1 and user_choice == 0:
    print("You lost, paper beats rock")
elif user_choice == computer_choice:
    print("It's a tie!!!")
else: 
    print("invalid")