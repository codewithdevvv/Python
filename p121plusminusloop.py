#even=minus
#odd=plus

a=0
b=0
num=int(input("Enter range:-"))
for i in range(1,num+1):
     if i % 2 == 0:
        print(i,end=" - ")
        a=a-i
     else:
       print(i,end=" + ")
       b=b+i
print(" \n sum of all num:-",a+b)
