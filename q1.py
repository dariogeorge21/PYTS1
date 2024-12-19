def calulate_record():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    oper=str(input("Enter the operator: "))
    if (oper=='+'):
        print("Sum of the numbers: ",num1+num2)
    elif (oper=='-'):
        print("Difference of the numbers: ",num1-num2)
    elif (oper=='*'):
        print("Multiplication of two numbers: ",num1*num2)
    elif (oper=='/'):
        print("Division of 2 numbers: ",num1/num2)
    elif (oper=='%'):
        print("Remainder of 2 numbers: ",num1%num2)
    else:
        print("Wrong Input")
    print("Thank you!!")
calulate_record()