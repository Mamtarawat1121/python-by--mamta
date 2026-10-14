nums = [34,78,99,77,88,56,45]
largest = nums[0]
n = len(nums)
for i in range(0,n):
    if nums[i]> largest:
        largest = nums[i]
print(largest)     



a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
c = int(input("enter a third number : "))
if a>=b and a>=c:
    print("largest number",a)
elif b>=a and b>=c:
    print("largrst number ", b) 
else:
    print("largest number ",c)    
