x={"zjj":123,"gzy":124}
x["gzy"]=125
x.update({"zjj":239,"gzy":129})
y={"hhh":193,"ajwi":1345}
z={**x,**y}
dict={"ahsjd":132,"akqw":234}

def average_scores(i):
    sum=0
    for s in i:
        sum=sum+s
        n=len(i)
        a=sum/n
        print("average scores is"+str(a))
        return
