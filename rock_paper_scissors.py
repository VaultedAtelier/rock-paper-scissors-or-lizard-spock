import random
from check_number import check_number
from logic import check_logic, check_other_logic

def play_again(): 
    while True: 
        answer = input("\nWould you like to play again? (y/n): ").lower() 
        if answer == "y": 
            return True 
        elif answer == "n": 
            return False 
        print("Please enter 'y' for yes or 'n' for no.")

while True:
    choice = check_number("\nPlease select between the following games: \n1. Rock, Paper, Scissors\n2. Rock, Paper, Scissors, Lizard, Spock\nGame Number Choice: ", 1, 2)

    if choice == 1:
        player = check_number("\n==============================\nRock ✊, Paper ✋, Scissors ✌️\n==============================\n\n1. '✊' (Rock)\n2. '✋' (Paper)\n3. '✌️' (Scissors)\nPick a number: ", 1, 3)
        computer = random.randint(1, 3)
        check_logic(player, computer)
        

    elif choice == 2:
        player = check_number("\n==============================\nRock ✊, Paper ✋, Scissors ✌️\n==============================\n\n1. '✊' (Rock)\n2. '✋' (Paper)\n3. '✌️' (Scissors)\n4. '🦎' (Lizard)\n5. '🖖' (Spock)\nPick a number: ", 1, 5)
        computer = random.randint(1, 5)
        check_other_logic(player, computer)

    if not play_again(): 
        print("\nThanks for playing!") 
        break