
import re 
text="- Tx_abbbtbmnkjhkhkh aaaaaaabaaab"
pattern="[a]+.*b$"
x=re.search(pattern,text)
if x:
    for i in range(x.start(),x.end()):
        print(text[i],end="")
else :
    print("no")
