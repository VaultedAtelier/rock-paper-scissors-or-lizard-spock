def check_logic(player, computer):

    choices = { 1: "✊", 2: "✋", 3: "✌️" } 
    print(f"\nYou chose: {choices[player]}") 
    print(f"CPU chose: {choices[computer]}")

    if player == computer:
        print("You have tied.")
    elif (
        (player == 1 and computer == 3)
        or (player == 2 and computer == 1)
        or (player == 3 and computer == 2)
    ):
        print("You won!")
    else:
        print("CPU has won.") 


def check_other_logic(player, computer):

    choices = { 1: "✊", 2: "✋", 3: "✌️", 4: "🦎", 5: "🖖" } 
    print(f"\nYou chose: {choices[player]}") 
    print(f"CPU chose: {choices[computer]}")

    if player == computer:
        print("You have tied.")
        return

    winning_combinations = {
        1: (3, 4),
        2: (1, 5),
        3: (2, 4),
        4: (2, 5),
        5: (1, 3),
    }

    if computer in winning_combinations[player]:
        print("You won!")
    else:
        print("CPU has won.")