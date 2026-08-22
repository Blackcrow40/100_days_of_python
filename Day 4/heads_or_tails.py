import random

def main():
    #! heads or tails
    head_count = 0
    tails_count = 0
    game = "y"
     
    while game == "y":
        num = random.randint(1,2)
        if num == 1:
            print("heads")
            head_count +=1 
            print(f"you have flipped {head_count} heads so far!")
            game = input("Would you like to flip again? (Y/N): ")
        else:
            print("tails")
            tails_count += 1
            print(f"you have flipped {tails_count} tails so far!")
            game = input("Would you like to flip again? (Y/N): ")
            
if __name__ == '__main__':
    main()
