a=0
b=0
num=int(input("Enter range:-"))
for i in range(1,num+1):
     if i % 2 == 0:
       print(i,"is even")
       a=a+i
     else:
        print(i,"is odd")
        b=b+i
print("Sum of all even no. =",a)
print("Sum of all odd no. =",b)
