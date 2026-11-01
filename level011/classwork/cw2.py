user_money = 500
transactions = 0
print ("====== BANK SYSTEM ======")
print ("1. Check Balance")
print ("2. Deposit Money")
print ("3. Withdraw Money")
print ("4. Transaction Summary")
print ("5. Exit")
print("=========================")
while True:
    choise = int(input("pick what do you vhant to do:"))
    if choise == 1:
        print("your balance is:", user_money)
    elif choise == 2:
        deposit = int(input("how much do you whant to deposit:"))
        if deposit >= 0:
           user_money += deposit
           transactions += 1
           print ("your balance now is:", user_money)
        else: 
            print("deposit amount need to be a posetive number")
    elif choise == 3:
        withdraw = int(input("how much do you want to withdraw:"))
        if withdraw >= 0:
            user_money -= withdraw
            transactions += 1
            print("withdraw sucsessful")
            print("your balance is:", user_money)
        elif user_money < withdraw:
            print("you do not have enought money")
        else:
            print("withdraw omaunt needs to be a posetive number")
    elif choise == 4:
        print(transactions)
    elif choise == 5:
        break
    else:
        print ("wrong chice try again")