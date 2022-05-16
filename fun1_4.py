def filter_prime(i):
    if ((i*i-1)%24==0 or i==2 or i==3) and i!=1:
        return i
a=list(map(int,input().split()))
t=""
for i in a:
    if(filter_prime(i)):
        t+=str(i)+" "
print(t)


