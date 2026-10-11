nums = [34,78,99,77,88,56,45]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]> largest:
        largest = nums[i]
print(largest)     