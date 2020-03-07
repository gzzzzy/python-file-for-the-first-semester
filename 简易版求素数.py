x=int(input("x是不是素数，x="))
assert x>1, "x必须大于1"
for s in range(2,x):
    if x%s==0:
        print('x不是素数')
        break
    else:
        print('x是素数')
