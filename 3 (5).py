a="abcdefghijklmnopqrstuvwxyz"

def toLowercase(t):
    for k in range(0,len(a)):
        if t==ord(a[k]):
            return a[k]
            return 
s=list(str(input()))
for i in range(0,len(s)):
    if ord(s[i])<91 and ord(s[i])>64:
        t=ord(s[i])+32
        s[i]= toLowercase(t)
t=""
for i in range(0,len(s)):
    t=t+s[i]
print(t)