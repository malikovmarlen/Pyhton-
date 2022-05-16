def Square(n):
    for i in range(n):
        yield pow(i,2)
n=int(input())
mygen=Square(n)
for i in mygen:
    print(i)