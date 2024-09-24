c=0
num=int(input("Enter the limit:-"))
for i in range(1,num):
    if i % 2 == 0:
        print(i,"is even")
        c=c+1
print("count=",c)