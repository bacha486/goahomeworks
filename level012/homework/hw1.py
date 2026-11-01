nums = [1, 4, 5, 84, 23]
print(nums[0])
print(nums[2])
print(nums[4])
for num in range(5):
    print(nums[num])
user_num = int(input("enter number:"))
if user_num in nums:
    print("this number is in the nums varuable")
else:
    print("this number is not in the nums varuable")