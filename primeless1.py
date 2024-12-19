n=int (input('Enter number: '))
l=[]
for i in range(2,n):
    c=True
    for j in range(2,i):
        if i%j==0:
            c=False
            break
    if c:
        l.append(i)
print(l)