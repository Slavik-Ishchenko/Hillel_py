import re

while True:
    password = input('Введите пароль: ')
    if len(password) <= 8:
        print('Пароль должен состоять из 8 и более символов, повторите ввод!')
        continue
    if not re.search(r'[a-z]', password):
        print('Пароль должен нести в себе как минимум 1 символ от a-z, повторите ввод!')
        continue
    if not re.search(r'[A-Z]', password):
        print('Пароль должен нести в себе как минимум 1 символ от A-Z, повторите ввод!')
        continue
    if not re.search(r'[0-9]', password):
        print('Пароль должен нести в себе как минимум 1 символ от 0-9, повторите ввод!')
        continue
    if not re.search(r'[$#@+=-]', password):
        print('Пароль должен нести в себе как минимум 1 символ из $#@+=-, повторите ввод!')
        continue
    break
print('Отличный пароль :)')
