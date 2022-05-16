def unique(i,t):
    
    if(t.count(str(i))==0):
        t+=str(i)+ " "
    return t

a=list(map(int,input().split()))
t=""
for i in a:
     t=unique(i,t)
print(t)