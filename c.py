n=int(input())
a=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==0:
            a[i][j]=j
        if j==0:
            a[i][j]=i
        if i==j:
            a[i][j]=i*j
for i in a:
    for j in i:
        print(j,end=' ')
    print() 