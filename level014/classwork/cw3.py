user_lists_num = int(input("enter number:"))
user_list = []
sum = 0
for i in range(user_lists_num):
    user_num = int(input("enter number in list:"))
    user_list.append(user_num)
for j in range(user_lists_num):
    sum += user_list[j]
print(sum)