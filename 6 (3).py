n=int(input())
for i in range(0,n):
    a=int(input())
    if a<=10:
        print("Go to work!")
    elif a>10 and a<=25:
        print("You are weak")
    elif a>25 and a<=45:
        print("Okay, fine")
    elif a>45:
        print("Burn! Burn! Burn Young!")