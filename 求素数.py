x=int(input("求1到x的素数，x="))
primenumber=[]
assert x>1, "x必须大于1" #断言
if x<=2:
    primenumber.append(2)
elif x<=3:
    primenumber.append(2)
    primenumber.append(3)
else:
    for b in range(2,x+1):
        primenumber.append(b)
    for a in range(4,x+1):
        for s in range(2,a):
            if a%s==0:
                primenumber.remove(a)
                break    
print(primenumber)

#判断一个正整数是否是素数
y=int(input('请输入一个正整数：'))
assert y in list(range(2,x+1)),"y必须在2和x之间"#断言
if y in primenumber:
    print(str(y)+"是素数")
else:
    print(str(y)+"不是素数")
            
                


            
