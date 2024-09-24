print("1)Square")
print("2)Cube")
do=int(input("What you wanna do:-"))
if do==1:
    no1=int(input("Enter from:-"))
    no2=int(input("Enter to:-"))
    for i in range(no1,no2+1):
        print("square of",i,"is:-",i*i)
elif do==2:
    no3=int(input("Enter from:-"))
    no4=int(input("Enter to:-"))
    for i in range(no3,no4+1):
        print("cube of",i,"is:-",i*i*i)
else:
    print("Choose thr correct option")
    