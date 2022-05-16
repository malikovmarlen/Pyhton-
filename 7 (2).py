import camelcase
test_str = 'geeksforgeeks_iS_best'
init,*temp = test_str.split('_')
c = camelcase.CamelCase()
s=""
for i in temp:
    t=c.hump(i)
    s=s+t
res = ''.join([init, s])
print(res)
