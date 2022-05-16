a=list(input())
b=str(input())
s=[]
for i in range(0,len(a)):
    if b==a[i]:
        s.append(i)
if len(s)==1 :
    print(s[0])
else:
    print(s[0],s[len(s)-1])