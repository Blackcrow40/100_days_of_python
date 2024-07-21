#TODO
# Add a point tracker

import random
hand = ["Rock", "Paper", "Scissors"]

def main():
    while True:
        player_hand = int(input("What do you choose?\n"
                                "1: for Rock\n"
                                "2: for Paper\n" 
                                "3: for Scissors\n"
                                "--> "))
        
        if player_hand == 1:
            print()
            print("You Chose Rock!")
            print(" - - - - - - - - - - - - - - ")
        
        elif player_hand == 2:
            print()
            print("You Chose Paper!")
            print(" - - - - - - - - - - - - - - ")
            
        elif player_hand == 3:
            print()
            print("You Chose Scissors!")
            print(" - - - - - - - - - - - - - - ")
        
        cpu_hand = random.choice(hand)
        print()
        print(f"Computer Chose {cpu_hand}")
        print(" - - - - - - - - - - - - - - ")
        
        # Rock (1)
        if cpu_hand == 'Rock': 
            if player_hand == 1:
                print("It Is A Draw")
            elif player_hand == 2:
                print("You Win!") 
            elif player_hand == 3:
                print("You lose!")       
            
            
        # Paper (2)
        elif cpu_hand == 'Paper':
            if player_hand == 1:
                print("You Lose!")
            elif player_hand == 2:
                print("It Is A Draw") 
            elif player_hand == 3:
                print("You Win!")   
                
        # Scissors (3)   
        elif cpu_hand == 'Scissors':    
            if player_hand == 1:
                print("You Lose!")
            elif player_hand == 2:
                print("You Win!") 
            elif player_hand == 3:
                print("It Is A Draw")     
    
        print()
    
if __name__ == "__main__":
    main()

