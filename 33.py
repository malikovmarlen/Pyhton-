a="dsfdsfsfdsfs"
b=a[::-1]
list=zip(a,b)
s=0
for i,j in zip(a,b):
    if i!=j:
        print('not p')
        exit()
print("p")