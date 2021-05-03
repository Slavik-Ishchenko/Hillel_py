def hide_email():
    s = str(input('Enter your email: '))
    left_side = s.replace(s[3:s.index('@')], '*' * len(s[3:s.index('@')]))
    right_side = left_side.replace(s[s.index('@')+1:-6], '*' * len(s[s.index('@')+4:-3]))
    return right_side


print(hide_email())
