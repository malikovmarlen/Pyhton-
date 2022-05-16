n=int(input())
a=[ [0]*n for i in range(n)]
if n%2==1:
    t=n-1
    for i in range(n):
        for j in range(n):
            if j>=t:
                a[i][j]='#'
            else:
                a[i][j]='.'
        t=t-1
else:
    t=0
    for i in range(n):
        for j in range(n):
            if j<=t:
                a[i][j]='#'
            else:
                a[i][j]='.'
        t=t+1 
for i in a:
    for j in i:
        print(j,end='')
    print() 