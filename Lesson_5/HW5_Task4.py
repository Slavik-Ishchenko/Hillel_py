from random import randint
lst = []
for i in range(15):
    lst.append(randint(-100, 500))
count = 0
for i in lst:
    if i % 2 != 0:
        lst[lst.index(i)] = 0
        count += 1
print(count)
print(lst)
