number = int(input("Enter a whole number: "))
while number < 0:
    print("Number must be positive.")
    number = int(input("Enter a positive whole number: "))
digits = 0
digit_sum = 0
even_count = 0
odd_count = 0
while number > 0:
    digit = number % 10
    digits += 1
    digit_sum += digit
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    number //= 10
print("Number of digits: " + str(digits))
print("Sum of digits: " + str(digit_sum))
print("Even digits: " + str(even_count))
print("Odd digits: " + str(odd_count))
if digit_sum % 2 == 0:
    print("The sum of digits is even.")
else:
    print("The sum of digits is odd.")