
import re 
text="454 tx fgfg"
pattern="[a]+[b]*"
x=re.search(pattern,text)
if x:
    print("yes")
else :
    print("no")
