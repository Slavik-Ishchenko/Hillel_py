def square_of_figure():
    c = str(input("Введите тип фигуры: "))
    a = int(input("Введите длину стороны 'A': "))
    if c == 'Квадрат':
        s = a ** 2
        return s
    if c == 'Треугольник':
        h = int(input("Введите длину стороны 'H': "))
        s = 0.5 * a * h
        return s


print(square_of_figure())
