from datetime import date


def is_date():
    d = str(input())
    d_new = list(d.split('.'))
    d_new.reverse()
    a = str(date.today())
    a_new = a.split('-')
    print(a_new == d_new)


is_date()
