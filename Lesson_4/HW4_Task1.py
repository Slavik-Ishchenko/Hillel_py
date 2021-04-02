x = int(input('Введите количество пройденных километров: '))
y = int(input('Введите количество дней: '))
kilometr = x
day = 1
while day != y:
    x += x * 0.1
    kilometr += x
    day += 1
print(kilometr)