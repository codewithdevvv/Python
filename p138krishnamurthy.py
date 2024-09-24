import math
x=int(input("Enter a number:-"))
num=x
t=0
while x>0:
    r=x%10
    t=t+math.factorial(r)
    x=x//10
if (num==t):
    print(t,"is krishnamurthy number")  
else:
    print(t,"is not a krishnamurthy number") 