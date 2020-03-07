m=int(input("m:"))
n=int(input("n:"))
y=""
for i in range(0,m):
    y=y+'*'
for i in range(0,n):
    x=''
    for j in range(1,n-i):
        x=x+" "
    print(x+y)

