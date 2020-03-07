grade1={'刘达':89,'王尔':95,'李珊':67,'陈思':75}
grade2={'刘达':75,'王尔':79,'李珊':79,'陈思':99}
grade3={'刘达':87,'陈思':91,'王尔':75,'陈思':98}
grade4={'刘达':89,'王尔':86,'陈思':99,'李珊':90}

def average_scores(i):
    sum=0
    for s in i:
        sum=sum+s
        n=len(i)
        a=sum/n
    return a

def dictolist(i):
    keys=[]
    values=[]
    for key,value in i.items():
        keys.append(key)
        values.append(value)
    return keys,values

def sorted_dict(keys,values):
    sorted_values=sorted(values,reverse=True)
    sorted_dict={}
    for i in sorted_values:
        rank=sorted_values.index(i)+1
        k=values.index(i)
        sorted_dict[keys[k]]=[i,rank]
    return sorted_dict

i=[]
names,scores1=dictolist(grade1)
names,scores2=dictolist(grade2)
names,scores3=dictolist(grade3)
names,scores4=dictolist(grade4)
name=input("请输入你的姓名:")
while name not in names:
    print("查无此人")
    name=input("请重新输入你的姓名:")
else:
    s1=grade1.get(name)
    i.append(s1)
    s2=grade2.get(name)
    i.append(s2)
    s3=grade3.get(name)
    i.append(s3)
    s4=grade4.get(name)
    i.append(s4)
    print("你的平均分是"+str(average_scores(i))+"分")
    sorted_grade1=sorted_dict(names,scores1)
    score1=sorted_grade1[name][0]
    rank1=sorted_grade1[name][1]
    print("你的grade1成绩是"+str(score1)+",排名第"+str(rank1))
    sorted_grade2=sorted_dict(names,scores2)
    score2=sorted_grade2[name][0]
    rank2=sorted_grade2[name][1]
    print("你的grade2成绩是"+str(score2)+",排名第"+str(rank2))
    sorted_grade3=sorted_dict(names,scores3)
    score3=sorted_grade3[name][0]
    rank3=sorted_grade3[name][1]
    print("你的grade3成绩是"+str(score3)+",排名第"+str(rank3))
    sorted_grade4=sorted_dict(names,scores4)
    score4=sorted_grade4[name][0]
    rank4=sorted_grade4[name][1]
    print("你的grade4成绩是"+str(score4)+",排名第"+str(rank4))
    
