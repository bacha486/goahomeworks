nums = [1, 23, 4, 7, 11, 29, 2, 8, 16, 12, 6, 3, 8, 5,24, 22, 70, 28, 10, 40]
odd_nums_sum = 0
even_nums_sum = 0
for i in range(20):
    oddornot = nums[i] % 2
    if oddornot == 0:
        even_nums_sum += nums[i] 
    else:
        odd_nums_sum += nums[i]
print("odd=" + str(odd_nums_sum))
print("even=" + str(even_nums_sum))
