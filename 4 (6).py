
import re 
text="- Tx_abbbtbmnkjhkhkh aaaaaaaa"
pattern="[A-Z]+[a-z]+"
x=re.search(pattern,text)
if x:
    for i in range(x.start(),x.end()):
        print(text[i],end="")
else :
    print("no")
