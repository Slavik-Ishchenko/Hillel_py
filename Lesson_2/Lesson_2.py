#1
name = str(input())
print('Hello, ' + name + '!')
#2
s = int(input('Please enter an integer number: '))
print('The next number for the number ' + str(s) + ' is ' + str(s+1))
print('The previous number for the number ' + str(s) + ' is ' + str(s-1))
#3
S = 100
v = int(input())
t = int(input())
if v > 0:
    print(v*t)
else:
    print(v*t)
#4
y = int(input())
if y % 4 == 0 and y % 400 == 0:
    print('YES')
elif y % 4 == 0 and y % 100 == 0 and y % 400 != 0:
    print('NO')
elif y % 4 == 0:
    print('YES')
else:
    print('NO')
#5
x = int(input())
if x > 0:
    print('sign(x) = 1')
elif x == 0:
    print('sign(x) = 0')
else:
    print('sign(x) = -1')
#6
x = float(input())
s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
if abs(x) in s:
    print('Yes')
#else:
    print('No')
#7
n = int(input('Input number of stars: '))
print('*' * n)