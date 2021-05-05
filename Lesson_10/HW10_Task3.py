n = int(input('Enter the number of shifts: '))
l_ = ['a', 'b', 'c', 'd', 'e', 'f']


def shift_list_(number, ls):
    empty = []
    if number > 0:
        if len(ls) > number > 0:
            number = len(ls) - number
            for i in reversed(ls[number:]):
                empty.append(i)
            for i in ls[:number]:
                empty.append(i)
    if number < 0:
        for i in ls[abs(number):]:
            empty.append(i)
        for i in (ls[:abs(number)]):
            empty.append(i)
    return empty


print(shift_list_(n, l_))
