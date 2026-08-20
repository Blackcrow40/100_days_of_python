    #  Tip Calcualtor (DAY2)
def main():
    print("Welcome to the Tip Calculator")
    total_bill = float(input("What was the total bill? $"))
    tip_perc = int(input("How much would you like to tip? 10, 12, or 15? "))
    num_peeps = int(input("How many people to split the bill? "))
    
    tip_total = tip_perc / 100
    tip_amount = total_bill * tip_total
    final_bill = total_bill + tip_amount
    split_cost = final_bill / num_peeps
    
    
    print(f"Each person shpuld pay ${split_cost:.2f}")
if __name__ == '__main__':
    main()
    #
