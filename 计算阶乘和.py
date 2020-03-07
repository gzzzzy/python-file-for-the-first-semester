def recursion(i):
    if i==1:
        return 1
    else:
        return i*recursion(i-1)
def main(i):
    if i==1:
        return 1
    else:
        return main(i-2)+recursion(i)
n=float(input("计算1!+3!+5!+...+n!=当n="))
assert n%2==1,"n必须为奇数正整数"
print("1!+3!+5!+...+n!="+str(main(n)))
    
