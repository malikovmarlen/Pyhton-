
import re 
text="txabbbtb mnkjhkhkh"
pattern="[a]+b{2}b?"
x=re.search(pattern,text)
if x:
    print("yes")
else :
    print("no")
