size=int(input("Enter the list size:-"))

listData=[]
list2=[]
list3=[]
for i in range(1,size+1):
    a=int(input("Enter value =>"))
    listData.append(a)

for x in listData:
    if x % 2 == 0: 
        list2.append(x)
    else:
        list3.append(x)

print(listData)
print("even numbers:-",list2)
print("odd numbers:-",list3)