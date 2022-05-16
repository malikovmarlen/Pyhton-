n=int(input())
t={}
for i in range(n):
    x=list(map(str,input().split(maxsplit=2)))
    t.setdefault(x[0],0)
    t[x[0]]=t[x[0]]+int(x[1])
a=max(t.values())
b=[]
for i,j in t.items():
    if j==a:
        b.append((i,"is lucky!"))
    else:
        b.append((i,"has to receive",a-j,"tenge"))
b.sort()
for i in b:
    print(*i)