import random
r = random.randint(1, 10)
n = int(input())
attempt = 1
if n == r:
    print('You won!')
else:
    while n != r and attempt != 3:
        n = int(input())
        attempt += 1
    if n != r:
        print('You lose!')
    else:
        print('You won!')