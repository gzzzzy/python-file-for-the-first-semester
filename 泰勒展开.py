x=int(input("计算e^x当x="))
s=1
c=0
for i in range(1,1000):
    for t in range(1,i+1):
        s=s*t
        r=1/s
        b=r*(x**i)
        c=c+b
print("e^x="+str(c+1))
