#统计每个人的平均成绩，并根据平均和每门成绩进行排序

grade1={'刘达':89,'王尔':95,'李珊':67,'陈思':75}
grade2={'刘达':75,'王尔':79,'李珊':80}
grade3={'李珊':87,'陈思':91,'张悟':75}
grade4={'刘达':89,'王尔':86,'张悟':99}

#先对每门课程成绩进行排序
#grade1
sub1grade1=[]#姓名
sub2grade1=[]#成绩
neworder1=[]#全新的排名
for key,value in grade1.items():
    sub1grade1.append(key)
    sub2grade1.append(value)
for each in list(sorted(sub2grade1,reverse=True)):
    neworder1.append(sub1grade1[sub2grade1.index(each)])

#grade2  #由于grade2里面有同学的成绩互相重复，需要提前处理

sub1grade2=[]#姓名
sub2grade2=[]#成绩
neworder2=[]#全新的排名
for key,value in grade2.items():
    sub1grade2.append(key)
    sub2grade2.append(value)
for each in list(sorted(sub2grade2,reverse=True)):
    neworder2.append(sub1grade2[sub2grade2.index(each)])
#for each in neworder2:
   # if neworder2.count(each)!=1:
        


#grade3
sub1grade3=[]#姓名
sub2grade3=[]#成绩
neworder3=[]#全新的排名
for key,value in grade3.items():
    sub1grade3.append(key)
    sub2grade3.append(value)
for each in list(sorted(sub2grade3,reverse=True)):
    neworder3.append(sub1grade3[sub2grade3.index(each)])

#grade4
sub1grade4=[]#姓名
sub2grade4=[]#成绩
neworder4=[]#全新的排名
for key,value in grade4.items():
    sub1grade4.append(key)
    sub2grade4.append(value)
for each in list(sorted(sub2grade4,reverse=True)):
    neworder4.append(sub1grade4[sub2grade4.index(each)])

#汇总每个学生的成绩
x=input('请输入你的姓名:')
average=[]#用来计算平均分
if grade1.get(x)!=None:
    average.append(grade1.get(x))
    print('你的grade1成绩是'+str(grade1.get(x))+',排名第'+str(neworder1.index(x)+1))
else:
    print(x+'，你是不是缺考了，grade1没你成绩哦！')
if grade2.get(x)!=None:
    average.append(grade2.get(x))
    print('你的grade2成绩是'+str(grade2.get(x))+',排名第'+str(neworder2.index(x)+1))
else:
    print(x+'，你是不是缺考了，grade2没你成绩哦！')
if grade3.get(x)!=None:
    average.append(grade3.get(x))
    print('你的grade3成绩是'+str(grade3.get(x))+',排名第'+str(neworder3.index(x)+1))
else:
    print(x+'，你是不是缺考了，grade3没你成绩哦！')
if grade4.get(x)!=None:
    average.append(grade4.get(x))
    print('你的grade4成绩是'+str(grade4.get(x))+',排名第'+str(neworder4.index(x)+1))
else:
    print(x+'，你是不是缺考了，grade4没你成绩哦！')

def average_scores(i):
    if len(i)==0:
        return '没成绩还想要平均分'
    else:
        sum=0
        for s in i:
            sum=sum+s
            n=len(i)
            a=sum/n
   # print("average scores is "+str(a))
        return '你的平均分为'+str(a)

#计算平均分排名
liuda=

print(average_scores(average))





