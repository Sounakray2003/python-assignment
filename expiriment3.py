n=4
b=[]
for a in range(0,n):
    a = int(input("Enter value: "))
    b.append(a)
print(b)
c=max(b)
print("Maximum value: ",c)
d=min(b)
print("Minimum value: ",d)
g=sum(b)
print("Sum of all the numbers: ",g)
avg=g/4
print("average of all the numbers: ",avg)