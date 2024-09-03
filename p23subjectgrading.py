maths=int(input("Enter your Maths marks"))
science=int(input("Enter your Science marks"))
english=int(input("Enter your English marks"))
total=maths+science+english
print(total,"is your total marks")
if total > 0 and total < 50:
    print("your grade is C!")
elif total >=50 and total < 100:
    print("your grade is B!")
else:
    print("you A!")