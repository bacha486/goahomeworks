rightpassword = "password123"
user_age = int(input("Enter your age: "))
password_guess = input("Enter the password: ")

print(user_age > 13 and password_guess == rightpassword)