start_string = str(input('Enter the start string: '))
old_word = str(input('Enter the old word: '))
new_word = str(input('Enter the new word: '))
number_of_replacements = str(input('Enter the number of replacements: '))


def change_string(start_str, old_w, new_w, number_of_replace):
    result_string = start_str.replace(old_w, new_w, int(number_of_replace))
    return result_string


print(change_string(start_string, old_word, new_word, number_of_replacements))