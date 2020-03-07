#you are given a list of names out of order ,please sort them in ascending order

items=['Sue','Beth','Cora','Ann','June','Tony','Lisa']


ALPHABET=[]
order=[]
newitems=[]

#创建字母表
for a in range(65,91):
    ALPHABET.append(chr(a))

for each in items:
    s=ALPHABET.index(each[0:1:])#表示首字母在字母表中的排序
    order.append(s)#order序列是应该拿来比较的数字

neworder=sorted(order)#排好升序的列表

for s in neworder:
    newitems.insert(neworder.index(s),items[order.index(s)])
print(newitems)

#如果人名不一定全是大写，可以使用：
#先建立一个新的空列表 Items=[]
#for each in items:
#   Items.append(each.(title))
#再用新的Items列表来做上面的内容即可


