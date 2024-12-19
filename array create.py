import numpy as np

a=int(input("Enter the number of rows: "))
b=int(input("Enter the number of columns: "))
ar=[]
for i in range(a):
    l=[]
    for j in range(b):
        c=int(input(f"Enter your {i+1}th row {j+1}th element: "))
        l.append(c)
    ar.append(l)
array=np.array(ar)
print(array)