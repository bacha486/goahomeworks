productprise = float(input("Enter the product price: "))
user_age = int(input("Enter your age: "))
print(" ")
mech_the_requaers = user_age > 18 and productprise > 100
print("You are older than 18 and the product price is greater than 100: " + str(mech_the_requaers))