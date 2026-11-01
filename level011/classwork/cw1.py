user_number = int(input("Enter your user number: "))
for i in range(1, 11):
    sum = user_number * i
    check = sum % 3
    if check == 0:
        print(user_number, "x", i, "=", sum , "is divideble by 3")
    elif check != 0:
        print(user_number, "x", i, "=", sum , "is not divideble by 3")