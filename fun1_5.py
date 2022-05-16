def perm(s):
    from itertools import permutations
    s=list(s)
    s.sort()
    return permutations(s)
s=str(input())
for i in list(perm(s)):
    for j in i:
        print(j,end="")
    print()
    