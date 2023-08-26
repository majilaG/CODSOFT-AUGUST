def calculator():
    opera= int(input("add opera  "))
    if(opera==1):
        n1=int(input("first number"))
        n2=int(input("second number"))
        print("sum ",n1+n2)
    elif(opera==2):
        n1=int(input("first number"))
        n2=int(input("second number"))
        print("subtraction ",n1-n2)
    elif(opera==3):
        n1=int(input("first number"))
        n2=int(input("second number"))
        print("multiplication ",n1*n2)
    elif(opera==4):
        n1=int(input("first number"))
        n2=int(input("second number"))
        print("divide ",n1/n2)
    elif(opera==5):
        n1=int(input("first number"))
        n2=int(input("second number"))
        print("module ",n1%n2)
    elif(opera==6):
        n1=int(input(" number for square"))
        print("square ",n1**2)
    else:
        print("invalid input")
    
calculator()

    
