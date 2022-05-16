def histogram(a):
    b=[]
    for i in a:
        t=""
        for j in range(i):
            t=t+'*'
        b.append(t)
    return b
a=list(map(int,input().split()))
t=histogram(a)
for i in t:
    print(i)
