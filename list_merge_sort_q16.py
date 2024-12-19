l=[]
a=int(input("Eneter the amount of elements in the list: "))
for i in range(a):
    b=int(input("Enter the element: "))
    l.append(b)
l.sort()

l2=[]
l3=[]
for i in l:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
final_list=l2+l3
print (final_list)