def CreateGenerator(n):
    for i in range(n):
        if i%2==0:
            yield i
n=int(input())
mygen=CreateGenerator(n)
for i in mygen:
    print(i)