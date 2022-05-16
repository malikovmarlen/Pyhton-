def CreateGenerator(n):
    for i in reversed(range(n)):
        yield i
n=int(input())
mygen=CreateGenerator(n)
for i in mygen:
    print(i)