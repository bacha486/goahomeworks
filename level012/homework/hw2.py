scores = [26, 79, 90, 39, 99]
passed = 0
failed = 0
for score in scores:
    print(score)
for score in scores:
    if score >= 50:
        passed += 1
    else:
        failed += 1
print("passed " + str(passed) + " students and failed " + str(failed))