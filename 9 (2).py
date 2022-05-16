n=int(input())
for i in range(0,n):
    a=str(input())
    s=""
    if a.rfind("@gmail.com")==len(a)-10:
        a=list(a)
        for i in range(0,len(a)-10):
            s=s+a[i]
    if len(s)>0:
        print(s)


