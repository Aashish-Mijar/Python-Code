import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move (Rock, Paper, Scissor): ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both user chose same!")
    print("Match tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock!")
        print("Computer wins!")
    
    else:
        print("Rock breaks Scissor!")
        print("You win!")


    
