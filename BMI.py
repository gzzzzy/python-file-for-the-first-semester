f=open("c:/health.txt",mode='r+')
content=f.readlines()

def BMI(x,y):     #y为体重，x为身高
    d=x*x
    s=y/d
    assert s>0,x!=0
    if s<float((content[1])[1:5]):
        print("您的BMI为"+str(round(s,ndigits=3))+','+(content[1])[6:8])
    elif s<float((content[2])[1:3]):
        print("您的BMI为"+str(round(s,ndigits=3))+','+(content[2])[4:6])
    elif s<float((content[3])[1:3]):
        print("您的BMI为"+str(round(s,ndigits=3))+','+(content[3])[4:6])
    elif s<float((content[4])[1:3]):
        print("您的BMI为"+str(round(s,ndigits=3))+','+(content[4])[4:6])
    else:
        print("您的BMI为"+str(round(s,ndigits=3))+','+(content[5])[4:8])

x=float(input("请输入你的身高（单位：m）:"))
y=int(input("请输入你的体重（单位：Kg）:"))
BMI(x,y)
print('附')
f.close()

f=open("c:/health.txt",mode='r+')
print(f.read())
f.close()



