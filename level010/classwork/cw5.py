students_quantity = int(input("how many students? "))
for i in range(1, students_quantity + 1):
    students_order = i
    students_score = int(input("whats your score: "))
    if students_score > 90 and students_score <= 100:
        str(students_order)
        print("student " + students_order + "score is:A")
    elif students_score > 80 and students_score <= 89:
        str(students_order)
        print("student " + students_order + "score is:B")
    elif students_score > 70 and students_score <= 79:
        str(students_order)
        print("student " + students_order + "score is:C")
    elif students_score > 60 and students_score <= 69:
        str(students_order)
        print("student " + students_order + "score is:D")
    elif students_score > 0 and students_score <= 59:
        str(students_order)
        print("student " + students_order + "score is:F")

    
