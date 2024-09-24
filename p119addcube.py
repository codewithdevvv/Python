a=0
num=int(input("Enter range="))
for i  in range(1,num+1):
   print(i*i*i,end=" + ")
   a=a+i*i*i
print(" \n addidtion of all the cube =",a)