x=0
y=0
num=int(input("Enter range:-"))
for i in range(1,num+1):
    if i % 2 == 0:
        print(i,"is even")
        x=x+1
    else:
        print(i,"is odd")
        y=y+1
print("even numbers=",x)
print("odd numbers=",y)
    