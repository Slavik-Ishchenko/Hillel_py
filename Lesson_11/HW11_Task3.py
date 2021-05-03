def max_number_of_letters():
    string = str(input('Enter the string: ')).split()
    _max_letter = string[0]
    for x in string:
        if len(_max_letter) < len(x):
            _max_letter = x
    return _max_letter


print(max_number_of_letters())
