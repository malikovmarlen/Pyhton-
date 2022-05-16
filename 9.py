import re
txt = "TheraininSpain"
x = re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
print(x)
