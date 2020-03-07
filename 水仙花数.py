flag=False
for n1 in range(1,10):
    for n2 in range(0,10):
        for n3 in range(0,10):
            for n4 in range(0,10):
                if n1*1000+n2*100+n3*10+n4==n1**4+n2**4+n3**4+n4**4:
                    print("四位数的水仙花数为"+str(n1*1000+n2*100+n3*10+n4))
                    flag=True
if flag==False:
    print("不存在四位数的水仙花数")
    
flag=False
for n1 in range(1,10):
    for n2 in range(0,10):
        for n3 in range(0,10):
            if n1*100+n2*10+n3==n1**3+n2**3+n3**3:
                print("三位数的水仙花数为"+str(n1*100+n2*10+n3))
                flag=True
if flag==False:
    print("不存在三位数的水仙花数")
    
               
                
