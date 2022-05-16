
import re
from tkinter import X 
text="- ..,,wTx_abbbtbmnkjhkhkh aaaaaaabaaab"
x=re.sub(",",":",text)
x=re.sub("[.]",":",x)
x=re.sub("\s",":",x)
print(x)
