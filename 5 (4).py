
def check(a):
    for i in range(2,a):
        if a%i==0:
             return False
    else:
            return True
a, b = map(int, input().split())

if b%2==0 and a<500 and check(a)==True:
    print("Good job!")     
else:
    print("Try next time!")