#给定一个多项式，用字典表示

polynomial={}
x=int(input('请输入多项式的阶数：'))
print('***************下面请输入多项式的各阶系数***************')
for i in range(x,-1,-1):
    s=int(input('请输入多项式的'+str(i)+'阶系数：'))
    assert s!=0,'该多项式任一系数都不能为0'
    polynomial['第'+str(i)+'阶系数']=s
print(polynomial)

#多项式之间的加法
print('***************下面进行两个多项式的加法***************')

x=int(input('请输入两个多项式的阶数：'))
#题目要求多项式任何系数都不能为0，实际上规定了两个多项式必须同阶

polynomial1={}
print('************下面请输入第一个多项式的各阶系数************')
for i in range(x,-1,-1):
    s=int(input('请输入第一个多项式的'+str(i)+'阶系数：'))
    assert s!=0,'该多项式任一系数都不能为0'
    polynomial1['第'+str(i)+'阶系数']=s

polynomial2={}
print('************下面请输入第二个多项式的各阶系数************')
for i in range(x,-1,-1):
    s=int(input('请输入第二个多项式的'+str(i)+'阶系数：'))
    assert s!=0,'该多项式任一系数都不能为0'
    polynomial2['第'+str(i)+'阶系数']=s

#下面进行加法
sum={}
for i in range(x,-1,-1):
    sum['第'+str(i)+'阶系数']=polynomial1['第'+str(i)+'阶系数']+polynomial2['第'+str(i)+'阶系数']
print('第一个多项式：')
print(polynomial1)
print('第二个多项式：')
print(polynomial2)
print('和：')
print(sum)


