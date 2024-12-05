#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def main():
    
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised: (COMMENT OUT HARD MODE TO USE)
    # #?LETTERS
    # password = ""
    # for char in range(1 , nr_letters +1):
    #     rand_char = random.choice(letters)
    #     password += rand_char
        
    # #?SYMBOLS
    # for char in range(1, nr_symbols +1):
    #     rand_symbol = random.choice(symbols)
    #     password += rand_symbol
    # #?NUMBERS
    # for char in range(1, nr_numbers +1):
    #     rand_num = random.choice(numbers)
    #     password += rand_num
        
    # print(password)
    
#Hard Level - Order of characters randomised:
     #?LETTERS
    password = []
    for char in range(1 , nr_letters +1):
        rand_char = random.choice(letters)
        password += rand_char
        
    #?SYMBOLS
    for char in range(1, nr_symbols +1):
        rand_symbol = random.choice(symbols)
        password += rand_symbol
    #?NUMBERS
    for char in range(1, nr_numbers +1):
        rand_num = random.choice(numbers)
        password += rand_num
        
    random.shuffle(password)    
    final_password = ""
    for char in password:
        final_password += char
    print(f "your Password is : {final_password}")
    
    
if __name__ == '__main__':
    main()
