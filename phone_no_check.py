n=int(input("Enter number: "))
if len(str(n))==10:
    if str(n)[0] in "987":
        print("Valid Phone Number")
else:
    print("Invalid Number!!")