balance = 500

while balance != 0:
    print("Balance is: ", balance)
    withdrawl_amount = float(input("Please enter withdrawl money: "))

    if withdrawl_amount > balance:
        print("Insufficient funds!") 
    elif withdrawl_amount <= 0:
        print("Invalid amount!")
    else:
        balance -= withdrawl_amount
        print("Successfully withdrawl!")