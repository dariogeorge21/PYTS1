n=int(input("Enter number: "))
fibbo_series=[]
a=0
b=1
for i in range(n):
    fibbo_series.append(a)
    a,b=b,a+b

for i in fibbo_series:
    print(i,end=" ")
