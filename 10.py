a=list(str(input()))
b=[]
for i in range(0,len(a)-1):
    if a[i]==' ':
        b.append(i)
t=0
s=""

for i in range(0,len(b)):
    if (b[i]-t)>2:
        for j in range(t,b[i]):
            s=s+a[j]
        s=s+" "
    t=0
    t=b[i]+1
if len(a)-b[len(b)-1]>3:
    for i in range(b[len(b)-1]+1,len(a)):
        s=s+a[i]    
print(s)