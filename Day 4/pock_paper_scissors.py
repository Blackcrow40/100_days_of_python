import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

all_choice = [rock, paper, scissors]

def main():
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    player_choice = input("")
    
    # Players pick what they want 
    if player_choice == "0":
        print(rock)
    elif player_choice == "1":
        print(paper)
    elif player_choice =="2":
        print(scissors)
        
    # the CPU picks what it is going to use at random 
    cpu_choice = random.choice(all_choice)
    print("Computer chose:")
    print(cpu_choice)
    
    # The winner is decided 
        # If the player chose rock
    if player_choice == "0":
        if cpu_choice == rock:
            print("It's a draw!")
        elif cpu_choice == paper:
            print("You lose!")
        elif cpu_choice == scissors:
            print("You win!")
        
        # If the player chose paper
    elif player_choice == "1":
        if cpu_choice == rock:
            print("You win!")
        elif cpu_choice == paper:
            print("It's a draw!")
        elif cpu_choice == scissors:
            print("You lose!")
        
        # If the player chose scissor
    elif player_choice == "2":
        if cpu_choice == rock:
            print("You lose!")
        elif cpu_choice == paper:
            print("You win!")
        elif cpu_choice == scissors:
            print("It's a draw!")
if __name__ == '__main__':
    main()
    
