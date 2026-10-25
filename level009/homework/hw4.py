num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
what_math_operation = (input("what mathematical operation do you whant to doe enter one of that simbols (+, -, *, /):"))
if what_math_operation == "+":
    print(num1 + num2)
elif what_math_operation == "-":
    print (num1 - num2)
elif what_math_operation == "*":
    print (num1 * num2)
else:
    print (num1 / num2)