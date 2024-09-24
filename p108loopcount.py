c=0
no1=int(input("Divisal of:-"))
no2=int(input("Enter limit:-"))

for i in range(1,no2+1):
    if i % no1==0:
        print(i,"is divisal of",no1)
        c=c+1
print("count=",c)