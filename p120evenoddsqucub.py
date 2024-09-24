#even=square
#odd=cube

a=0
b=0
num=int(input("Enter range:-"))
for i in range(1,num+1):
     if i % 2 == 0:
        print(i*i,end=" + ")
        a=a+i*i
     else:
       print(i*i*i,end=" + ")
       b=b+i*i*i
print("sum off all num:-",a+b)
