def main():
    
    print()
    print(" -   -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -")
    print()
    print("                   Welcome To The Tip Calculator!")
    print()
    print(" -   -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -")
    print()
    
    total = float(input("What is the bill total? :  "))
    print()
    print(" -   -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -")
    print()
    tip = int(input("What Tip Amount Would You Like? 10%, 12%, 15% :  "))
    print()
    print(" -   -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -")
    print()
    split = int(input("How many peaple are spliting the bill? : "))
    print()
    print(" -   -   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - -  -  -")
    print()
    
    tip_total = (tip/100) * total + total
    split_total =  tip_total / split
    final_split = round(split_total, 2)
    round_total = round(tip_total, 2)
    print(f"The total including tip is {round_total}")
    print()
    print(f"Each person pays {final_split}")
    print()
    
    

if __name__ == "__main__":
    main()
