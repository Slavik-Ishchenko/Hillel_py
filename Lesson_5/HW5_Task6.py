def empty_del(d):
    d1 = {k: v for k, v in d.items() if v is not None}
    print(d1)


empty_del()