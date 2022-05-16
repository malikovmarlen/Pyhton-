color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('sdfdsfdfd.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('sdfdsfdfd.txt')
print(content.read())