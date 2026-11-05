smallest = 0
largest = 0
positive = 0
negative = 0
zero = 0
total = 0

for i in range(15):
    number = float(input("Enter number " + str(i + 1) + ": "))

    if i == 0:
        largest = number
        smallest = number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

    total += number
average = total / 15

print("Largest : " + str(largest))
print("Smallest : " + str(smallest))
print("Positive : " + str(positive))
print("Negative : " + str(negative))
print("Zeros: " + str(zero))
print("Average: " + str(average))

if average > 0:
    print("The average is positive.")
elif average < 0:
    print("The average is negative.")
else:
    print("The average is zero.")