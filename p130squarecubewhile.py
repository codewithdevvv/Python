while True:
    print("1)Square")
    print("2)Cube")
    print("3)Exit")
    do=int(input("What you wanna do:-"))
    if do==1:
        num=int(input("Square of?:-"))
        print("Square of",num,"is = ",num*num)
    elif do==2:
        num=int(input("Cube of?:-"))
        print("Cube of",num,"is = ",num*num*num)
    elif do==3:
        print("bye!!")
        break
    else:
        print("Choose the correct option!")