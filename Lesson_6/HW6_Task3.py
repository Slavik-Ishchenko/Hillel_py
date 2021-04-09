s = ['a', 'b', 'c', 'd', 'e']
d = {}
for i in s:
    d.setdefault(s.index(i), i)
print(d)

