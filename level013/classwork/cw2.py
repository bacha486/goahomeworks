user_num = int(input("enter number:"))
piramid = user_num
for i in range(1, user_num + 1):
    for j in range(piramid - 1):
        print(end=" ")
    piramid -= 1
    print(i)
    for q in range(1, i + 1 ):
        print()
    