b=int(input())
x=list(map(int,(input().split(maxsplit=b))))
    
max=0
ma=0
for i in range(b):
    if x[i]>max:
        max=x[i]
        t=i
for i in range(b):
    if x[i]>ma and x[i]<=max and i!=t:
        ma=x[i]
print(ma*max)
