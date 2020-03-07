
class Person(object):
    num_of_persons=0#类属性：记录人的实例个数
    def __init__(self,name,gender,height,weight):
         self.name=name
         self.gender=gender
         self.height=height
         self.weight=weight
         Person.num_of_persons+=1

    def introduce_oneself(self):
        print("我的名字叫{},我是一位{}士,身高{}cm，体重{}kg。".format(self.name,self.gender,self.height,self.weight))

    @classmethod
    def get_num_of_persons(cls):
        return cls.num_of_persons

zjj=Person("周经纪","男",180,70)
zyx=Person("张义祥","男",170,60)
zjj.introduce_oneself()
zyx.introduce_oneself()
print("目前Person类已创建{}个实例".format(Person.get_num_of_persons()))

