a=int(input())
b=str(input())
if b=='k':
    c=str(input())
    s="{:."+c+"f}"
    print(s.format(a/1024)) 
else:
    print(a*1024)   