import re
text='WrtYfdgdgyT'
x=re.sub(r"([a-z])([A-Z])",r"\1_\2",text)
x=x.lower()
print(x)