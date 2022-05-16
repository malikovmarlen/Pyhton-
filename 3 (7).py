
import re 
text="- tx_abbbtbmnkjhkhkh aaaaaaaa"
pattern="[a-z]+_+[a-z]+"
x=re.search(pattern,text)
if x:
    for i in range(x.start(),x.end()):
        print(text[i],end="")
else :
    print("no")
