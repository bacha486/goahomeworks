secret_num = 123
gueses_num = 0
user_guess = int(input("Guess a number: "))
while user_guess != secret_num:
    if user_guess > secret_num:
        print("Too high!")
        user_guess = int(input("Guess again: "))
        gueses_num += 1
    elif user_guess < secret_num:
        print("Too low!")
        user_guess = int(input("Guess again: "))
        gueses_num += 1

print("You win!")
print("youre gussed the number in", gueses_num, "guesses")