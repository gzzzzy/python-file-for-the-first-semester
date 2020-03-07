x=int(input('请输入一个正整数：'))
primenumber=list(range(2,x+1))
for each in primenumber:
    for s in range(4,each):
        if each%s==0:
            primenumber.remove(each)
            break
primenumber.insert(0,2)
print(primenumber)
