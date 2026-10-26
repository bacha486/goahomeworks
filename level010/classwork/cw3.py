correct_password = "123aaaeee"
user_guess = input('enter the password:')
while user_guess != correct_password:
    print ("WRONG! try again")
    user_guess = input('enter the password:')
print("accses granted")
