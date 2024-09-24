a=1
n=int(input("Enter range:-"))
for i in range(1,n+1):
    print(i,end=" x ")
    a=a*i
print("\n = ",a)