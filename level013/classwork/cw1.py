user_num = int(input("enter a number:"))
cicles = user_num
for i in range(user_num):
    for num in range(cicles):
        piramid = str(user_num) + str(user_num - num)
        cicles -= 1
    print (piramid)
        
