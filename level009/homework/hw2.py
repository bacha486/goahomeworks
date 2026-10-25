user_score = int(input("whats youre score?"))
if user_score > 90 and user_score <= 100:
    print("your score is:A")
elif user_score > 80 and user_score <= 89:
    print("your score is:B")
elif user_score > 70 and user_score <= 79:
    print("your score is:C")
elif user_score > 60 and user_score <= 69:
    print("your score is:D")
elif user_score >= 0 and user_score <= 59:
    print("your score is:F")
else:
    print("you printed wrong score:ERROR")