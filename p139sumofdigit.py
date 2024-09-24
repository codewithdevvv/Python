num=int(input("Enter the Number:-"))
sum = 0
while num > 0:
    sum += num % 10  
    num //= 10  
print("The sum of digits is:", sum)
