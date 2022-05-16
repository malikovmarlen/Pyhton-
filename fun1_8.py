def spy_game(a):
    s=0
    t=0
    for i in range(len(a)):
        if a[i]==0:
            t=i
            s+=1
        elif a[i]==7 and i>t and s>=2:
            return True
a=list(map(int,input().split()))
if(spy_game(a)):
    print("True")
else: print("False")