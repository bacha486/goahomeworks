user_num = int(input("enter a integer number: "))
for i in range(1, user_num + 1):
    chek_oddornot = i % 2
    if chek_oddornot == 0:
        print(str(i) + " even")
    else:
        print(str(i) + " odd")