print("1)add 1 to 10")
print("2)mul 1 to 10")
print("3)div 1 to 10")
print("4)sub 1 to 10")
do=int(input("what you wanna do:-"))
for i in range(1,10):
 if do==1:
   print(i,i+i)
 elif do==2:
   print(i*i)
 elif do==3:
   print(i/i)
 elif do==4:
   print(i-i)
 else:
   print("choose the correct option")
   break
