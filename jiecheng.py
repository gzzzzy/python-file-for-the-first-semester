def jie(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    return s
    

if __name__=="__main__":
    x=int(input("求x!当x="))
    print(str(jie(x)))
