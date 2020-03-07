def recursion(i):
    if i==0:
        return (s+1)*2
    else:
        return (recursion(i-1)+1)*2

x=int(input("小猴吃了多少天："))
s=int(input("最后一天剩多少个："))
k=recursion(x-2)
print("小猴共有"+str(k)+"个桃")
