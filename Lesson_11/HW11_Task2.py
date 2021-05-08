def hide_email():
    s = str(input('Enter your email: '))
    dog = s.index('@')
    left_side = s.replace(s[3:dog], '*' * len(s[3:dog]))
    right_side = left_side.replace(s[dog+1:-6], '*' * len(s[dog+4:-3]))
    return right_side


print(hide_email())
