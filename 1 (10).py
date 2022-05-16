import os 
s = input()
def printt(path):
    for x in os.listdir(path):
        print (x)
printt(s)
