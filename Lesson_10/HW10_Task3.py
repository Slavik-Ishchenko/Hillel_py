n = int(input('Enter number: '))
lst = list(map(int, input('Enter the list values separated by commas: ').split(',')))


def move_list(number, ls):
    empty = []
    if n <= 0:
        for i in range(abs(n)):
            empty.append(n)
        print(lst+empty)
    else:
        for i in range(n):
            empty.append(n)
        print(empty+lst)


move_list(n, lst)
