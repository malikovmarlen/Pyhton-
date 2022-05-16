def has_33(a):
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            return True
a=list(map(int,input().split()))
if(has_33(a)):
    print("True")
else: print("False")
    