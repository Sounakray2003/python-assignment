row = int(input("Enter of rows: "))
k = row-1
for i in range(0,row):
    for j in range(0,k+1):
     print("",end=" ")
    k=k-1
    for j in range(i):
       print("*",end=" ")
    print()