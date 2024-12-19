#This is the lab work of S1



#Write a python program to find the area of triangle?
def tr_area():
    height=int(input("Enter height: "))
    base=int(input("Enter base: "))
    area=0.5*base*height
    print("Area of the triange: ",area)


def sq_area():
    side=int(input("Enter side length: "))
    area=pow(side,2)
    print("Area of square: ",area)
# sq_area()
#Find the square of a number
def sq_num():
    a=int(input("zenter a number: "))
    sq=pow(a,2)
    print("Square of the number: ",sq)
    pass


def pattern():
    n=int(input("Enter num: "))
    for i in range(1,n+1,1):
        for j in range(1,i,1):
            print("*",end='')
        print()
    for i in range(n+1,1,-1):
        for j in range(i,1,-1):
            print("*",end='')
        print()
# pattern()

def math():
    import math as mt
    a=int(input("Enter a number: "))
    sqrt=mt.sqrt(a)
    print("Suare root of ",a," = ",sqrt)
# math()

def area_cirlce():
    radi=int(input("Enter the radius: "))
    area=3.14*radi*radi
    circum=3.14*2*radi
    print("Circumference of circle :",circum)
    print("Area of circle: ",area)
# area_cirlce()    


def factorial():
    num=int(input("Enter a number: "))
    factorial=1
    for i in range(2,num+1,1):
        factorial=factorial*i
    print("Factorial of a number: ",factorial)
# factorial()

def case_example(value):
    match value:
        case 1:
            return "It's one!"
        case 2:
            return "It's two!"
        case 3:
            return "It's three!"
        case _:
            return "It's something else!"

def calculator():
    def addition():
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        sum=num1+num2
        print(sum)
    def subtraction():
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        diff=num1-num2
        print(diff)
    def multiply():
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        pro=num1*num2
        print(pro)
    def division():
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        div=num1/num2
        print(div)
    def exponent():
        base=int(input("Enter a base: "))
        pow=int(input("Enter power: "))
        exp=base*pow
        print(exp)

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
# calulate_record()


#i=pnr
def simple_interest():
    pr_amount=int(input("Enter the principle amount: "))
    no=int(input("Enter the no of months: "))
    rate=float(input("Enter the amount of interest: "))
    sim_int=(pr_amount*no*rate)/100
    print("Simple Interest: ",sim_int)
# simple_interest()

def small_integer():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    num3=int(input("Enter the third number: "))
    
    smallest=num1
    if num2<smallest:
        smallest=num2
    if num3<smallest:
        smallest=num3
    print(smallest)
    
small_integer()


# To print the color based on the code value conditions 
#1. R for red color 
#2. B for Blue
#3. G for Green
# Any other value wrong call

def color_code():
    code=str(input("Enter code of color: "))
    if code=='R':
        print("RED")
    elif code=='B':
        print("BLUE")
    elif code=='G':
        print("GREEN")
    else:
        print("Wrong Input")