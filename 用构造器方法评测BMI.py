class Health():#评测BMI
    def __init__(self,height,weight):
        self.height=height #身高（单位：厘米）
        self.weight=weight #体重（单位：公斤）

    def get_BMI(self):
        BMI=self.weight/(self.height**2)
        if BMI<18.5:
            result=[BMI,'过轻']
        elif BMI<24:
            result=[BMI,'正常']
        elif BMI<27:
            result=[BMI,'过重']
        elif BMI<32:
            result=[BMI,'肥胖']
        else:
            result=[BMI,'过度肥胖']
        return result

    def show_BMI(self):
        x=self.get_BMI()
        print('BMI是{},显示{}。'.format(round(x[0],ndigits=3),x[1]))

class Person(object):
    num_of_persons=0
    
    def __init__(self,name,age,institute,ID,grade):
        self.name=name#姓名
        self.age=age#年龄
        self.institute=institute#学院
        self.ID=ID#学号
        self.grade=grade#年级
        Person.num_of_persons+=1

    @classmethod
    def get_num_of_persons(cls):
        return cls.num_of_persons
    
    def output(self):
        print('{}\t{}岁\t{}\t学号：{}\t大{}'.format(self.name,self.age,self.institute,self.ID,self.grade))

x=input('请输入你的姓名：')
y=input('请输入你的年龄：')
z=input('请输入你的学院：')
a=input('请输入你的学号：')
b=input('请输入你的年级：')
c=float(input('请输入你的身高（单位：米）：'))
d=float(input('请输入你的体重（单位：千克）：'))

person=Person(x,y,z,a,b)
person.output()
bmi=Health(c,d)
bmi.show_BMI()
#gzy=Person('高智宇','18','金融学院','2019310410','一')
#GZY=Health(1.76,65)
#gzy.output()
#GZY.show_BMI()
    
