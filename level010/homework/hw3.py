money = float(input("Enter your money: "))
while money <= 0:
    print("Money must be positive.")
    money = float(input("Enter your money: "))
total = 0

while True:
    answer = input("Add an item? (yes/no): ")
    if answer == "no":
        break
    price = float(input("Price: "))
    while price <= 0:
        print("Price must be positive.")
        price = float(input("Price: "))

    quantity = int(input("Quantity: "))
    while quantity <= 0:
        print("Quantity must be positive.")
        quantity = int(input("Quantity: "))

    item_total = price * quantity
    total = total + item_total
    print("Item total:", item_total)
    print("Cart total:", total)

if total >= 200:
    discount = total * 0.15
elif total >= 100:
    discount = total * 0.10
else:
    discount = 0
final = total - discount
print("Initial amount:", total)
print("Discount:", discount)
print("Final amount:", final)
if money >= final:
    print("Money left:", money - final)
else:
    print("You don't have enough money.")