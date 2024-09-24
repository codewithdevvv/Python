x=int(input("Enter a number:-"))
num=x
t=0
while x>0:
    r=x%10
    t=t*10+r
    x=x//10
if (num==t):
    print(t,"is palindrome number")  
else:
    print(t,"is not a palindrome number") 