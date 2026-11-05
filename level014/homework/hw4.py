start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

while start > end:
    print("Start must not be bigger than end.")
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
fizz = 0
buzz = 0
fizzbuzz = 0
for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + " FizzBuzz")
        fizzbuzz += 1
    elif number % 3 == 0:
        print(str(number) + " Fizz")
        fizz += 1
    elif number % 5 == 0:
        print(str(number) + " Buzz")
        buzz += 1
print("Fizz: " + str(fizz))
print("Buzz: " + str(buzz))
print("FizzBuzz: " + str(fizzbuzz))