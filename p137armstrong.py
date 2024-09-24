x=int(input("Enter a number:-"))
num=x
t=0
while x>0:
    r=x%10
    t=t+r*r*r
    x=x//10
if (num==t):
    print(t,"is armstrong number")  
else:
    print(t,"is not a armstrong number") 