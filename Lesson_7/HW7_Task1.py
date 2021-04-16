s = str(input())


def output_by_element(func):
    def inner(*args, **kwargs):
        elements = list(s.split(' '))
        print(elements)
        func()

    return inner()


@output_by_element
def output_by_string():
    return s
