a=str(input())
a=list(a)
s=0
for i in range(0,len(a)):
    s=s+(ord(a[i])-48)*pow(2,len(a)-i-1)
print(s)
