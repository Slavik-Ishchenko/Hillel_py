s = ['a', 'b', 'c', 'd', 'e']
d = {}
for i in enumerate(s):
    d.setdefault(i[0], i[1])
print(d)
