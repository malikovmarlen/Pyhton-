a = list(str(input()))
sum = 0
for i in a:
    sum=sum+ord(i)
if sum>300:
    print("It is tasty!")
else:
    print("Oh, no!")