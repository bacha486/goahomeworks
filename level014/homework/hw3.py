answer = 37
attempts = 7
guessed = False

for i in range(attempts):
    guess = int(input("Enter your guess you have "+ str(attempts - i )+" attempts left: "))

    if guess == answer:
        guessed = True
        break
    elif guess < answer:
        print("The secret number is bigger.")
    else:
        print("The secret number is smaller.")
if guessed:
    print("Congratulations! You guessed the number!")
else:
    print("Game over! The secret number was " + str(answer))