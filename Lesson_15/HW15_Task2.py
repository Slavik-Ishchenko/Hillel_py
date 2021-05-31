import re


def format_number(ready_number):
    global res
    replace_values = {"+38": "", "38": "", "-": "", " ": ""}  # переделал номер в единый формат
    for key, value in replace_values.items():
        ready_number = ready_number.replace(key, value)
        res = re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'(+38) \1 \2-\3-\4', ready_number)
    return res


print(format_number('380639999999'))
