correct_password = "abcd123"
incorect_trys = 0
user_guess = input("enter a password:")
while incorect_trys > 4 and correct_password != user_guess:
    incorect_trys =+ 1
    print("WRONG! try again")
    user_guess = input("enter a password:")
if user_guess == correct_password:
    print("acsess granted ")