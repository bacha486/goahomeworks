total_tickets = 0
total_initial = 0
total_discount = 0

while True:
    answer = input("Buy tickets? (yes/no): ")
    if answer == "no":
        break
    age = int(input("Age: "))
    if age < 0:
        print("Invalid data.")
    else:
        if age < 12:
            price = 10
        elif age >= 60:
            price = 12
        else:
            price = 15
        print("Ticket price:", price)
        quantity = int(input("Number of tickets: "))
        if quantity <= 0:
            print("Invalid data.")
        else:
            if quantity >= 5:
                percent = 0.20
            elif quantity >= 3:
                percent = 0.10
            else:
                percent = 0
            initial = price * quantity
            discount = initial * percent
            total_tickets = total_tickets + quantity
            total_initial = total_initial + initial
            total_discount = total_discount + discount
            print("Purchase cost:", initial - discount)

final = total_initial - total_discount
print("Total tickets:", total_tickets)
print("Initial amount:", total_initial)
print("Discount:", discount_total if False else total_discount)
print("Final amount:", final)