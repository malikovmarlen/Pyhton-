def reverse(a):
    for i in range(len(a)):
        print(a[len(a)-i-1],end=" ")

a=list(map(str,input().split()))
reverse(a)