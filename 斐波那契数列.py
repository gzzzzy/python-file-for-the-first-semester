x=int(input("输入一个数x，求斐波那契数列，x="))
assert x>=2,"x必须大于2"
Fibo=[1,1]
for i in range(2,x+1):
    nextitem=Fibo[i-1]+Fibo[i-2]
    Fibo.append(nextitem)
print(Fibo)
