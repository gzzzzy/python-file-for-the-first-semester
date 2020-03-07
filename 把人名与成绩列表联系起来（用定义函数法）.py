#通过两个列表建立字典
def builtdict(keys,values):#keys和values必须是两个列表
    artdict={}
    for i in keys:
        artdict[i]=values[keys.index(i)]
    return artdict

#主程序
classmates=['刘达','王尔','李珊','陈思']
scores=['89','96','87','90']
grades=builtdict(classmates,scores)
print(grades)
