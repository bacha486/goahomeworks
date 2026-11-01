numbers = [0, 0, 0, 0, 0, 0, 0]

for i in range(7):
    numbers[i] = int(input("Enter number " + str(i + 1) + ": "))
print()
print("Entered numbers:")
for num in numbers:
    print(num)
positive = 0
negative = 0
zero = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)