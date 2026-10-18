item_cost = float(input("how much the item costs?: "))
money_have = float(input("how much money do you have?: "))
print(" ")
can_buy = item_cost <= money_have
if can_buy == True:
    print("you can buy the item continue to checkout")
else:
    print("you can't buy this item ")
