def CreateGenerator(n):
    for i in range(n):
        yield i*i
n=int(input())
mygen=CreateGenerator(n)
for i in mygen:
    if i<=20:
        print(i)