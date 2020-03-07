p=int(input("请输入任意正整数p:"))
q=int(input("请输入任意正整数q:"))
for a in range(min(p,q),0,-1):
    if p%a==0 and q%a==0:
        print("p和q的最大公约数是"+str(a))
        break
        
