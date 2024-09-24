sub1=int(input("Enter your Maths marks"))
sub2=int(input("Enter your English marks"))
sub3=int(input("Enter your Science marks"))
result=sub1+sub2+sub3
if result > 0 and result < 50:
    print("your grade is C!")
elif result >=50 and result < 100:
    print("your grade is B!")
else:
    print("you A!")