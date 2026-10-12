product_name = input('Enter product name: ')
product_price = float(input('Enter product price: '))
product_quantity = int(input('Enter product quantity: '))
total_price = product_price * product_quantity
print(" ")
print('Product name: ' + product_name)
print('Product price: $' + str(product_price))
print('Product quantity: ' + str(product_quantity))
print('Total price: $' + str(total_price))