#求最大公约数
def hcf(x,y):
    for a in range(min(x,y),0,-1):
        if x%a==0 and y%a==0:
            return a
            break
 

#求最小公倍数
#利用最大公约数来求
def lcm(x,y):
    s=hcf(x,y)*(x/hcf(x,y))*(y/hcf(x,y))
    return s
            
print('*'*15+'求两个数的最大公约数和最小公倍数'+'*'*15)
x=int(input("请输入一个正整数："))
y=int(input("请输入一个正整数："))
a=hcf(x,y)
print('最大公约数为'+str(a))
b=round(lcm(x,y))
print('最小公倍数为'+str(b))
