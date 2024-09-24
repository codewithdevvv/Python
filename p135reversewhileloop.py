x=int(input("Enter a number:-"))
t=0
while x>0:
    r=x%10
    t=t*10+r
    x=x//10
print("Reverse no.:-",t)    