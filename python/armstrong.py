num = int(input("Enter number: "))
temp = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** len(str(temp))
    num //= 10

if total == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong")