balance = 500
transactions = 0

while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Number of transactions")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance = balance + amount
            transactions = transactions + 1
            print("Deposit successful.")
            print("Balance:", balance)
    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("You don't have enough money.")
        else:
            balance = balance - amount
            transactions = transactions + 1
            print("Withdrawal successful.")
            print("Balance:", balance)
    elif choice == "4":
        print("Successful transactions:", transactions)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")

print("Successful transactions:", transactions)
print("Final balance:", balance)