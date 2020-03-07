def parallelogram(m,n):#m行n列
    y=' '
    for s in range(1,m+1):
        a=y*(m-s)+'*'*(m)
        print(a)

    
x=int(input("x（行）:"))
y=int(input("y（列）:"))
parallelogram(x,y)
