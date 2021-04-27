def new_file():
    a = str(input())
    string = []
    while a != '':
        a = str(input())
        string.append(a)
    with open('new_file.txt', 'w') as file:
        for i in string:
            file.write(i + '\n')


new_file()
