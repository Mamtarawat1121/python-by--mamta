nums = [99, 67,54,43,23,11]
smallest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]<smallest:
        smallest = nums[i]
print(smallest)        
