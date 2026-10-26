user_age = int(input("enter your age: "))
if user_age < 13:
    print ("user is child")
elif user_age >= 13 and user_age <= 17:
    print("user is teenage")
else: 
    print("user is adult")