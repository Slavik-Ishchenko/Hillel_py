s = str(input())


def palindrom(st):
    if len(s) % 2 == 0:
        left_side = s[:len(s)//2]
        right_side = s[len(s)//2:][::-1]
        print(left_side == right_side)
    else:
        left_side = s[:len(s) // 2]
        right_side = s[(len(s) // 2) + 1:][::-1]
        print(left_side == right_side)


palindrom(s)
