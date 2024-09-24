held=int(input("Number of classes held:-"))
attended=int(input("Number of classes attended:-"))
print(attended/held*100,"% is your total attendence")
if attended/held*100 > 75:
    print("Your are allowed to sit in exams!")
else:
    print("Your are not allowed to sit in exams!")