import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move (Rock, Paper, Scissor): ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")