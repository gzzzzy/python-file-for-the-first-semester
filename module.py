from module1 import repeat as r1
print('__name__ in module is %s'%__name__)
from module2 import repeat as r2
from jiecheng import jie
if __name__=="__main__":
    repeat=int(jie(r1))+int(jie(r2))
    print("repeat="+str(repeat))

from average_scores import *
average_scores([r1,r2])


