import string, os
if not os.path.exists("sss.txt"):
   os.makedirs("sss.txt")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)