user_num = int(input("enter a number:"))
num_oddornot = user_num % 2
if user_num > 0:
    print ("number is greater than 0")
elif user_num < 0:
    print("number is lower than 0")
else:
    print("number is equal to 0")
if num_oddornot == 0:
    print("and it is even")
else:
    print("and it is odd")