s = str(input())


def palindrom(st):
    if len(st) % 2 == 0:
        left_side = st[:len(st)//2]
        right_side = st[len(st)//2:][::-1]
        print(left_side == right_side)
    else:
        left_side = st[:len(st) // 2]
        right_side = st[(len(st) // 2) + 1:][::-1]
        print(left_side == right_side)


palindrom(s)
