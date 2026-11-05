user_lists_num = int(input("enter number:"))
users_score = []
sum = 0
for i in range(user_lists_num):
    user_num = int(input("enter "+ str(i + 1) + " students score:"))
    if user_num < 0 or user_num > 100:
        user_num = int(input("enter "+ str(i + 1) + " students score:"))
    users_score.append(user_num)