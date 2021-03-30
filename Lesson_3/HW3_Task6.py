fir_p = str(input('ВВедите номер начальной клетки по вертикали и по горизонтали (через запятую): '))
sec_p = str(input('ВВедите номер конечной клетки по вертикали и по горизонтали (через запятую): '))
if int(fir_p[0]) > 8 or int(fir_p[2]) > 8 or int(sec_p[0]) > 8 or int(sec_p[2]) > 8:
    print("No")
else:
    if int(sec_p[0]) - 1 == int(fir_p[0]) and int(sec_p[2]) - 2 == int(fir_p[2]) or int(sec_p[0]) - 2 == int(fir_p[0]) and int(sec_p[2]) - 1 == int(fir_p[2]):
        print("Yes")
    elif int(sec_p[0]) + 1 == int(fir_p[0]) and int(sec_p[2]) + 2 == int(fir_p[2]) or int(sec_p[0]) + 2 == int(fir_p[0]) and int(sec_p[2]) + 1 == int(fir_p[2]):
        print("Yes")

    else:
        print("No")