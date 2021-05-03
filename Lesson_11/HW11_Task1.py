win = int(input('Enter the number of wins: '))
draw = int(input('Enter the number of draws: '))
loss = int(input('Enter the number of defeats: '))


def scoring(w, d, l):
    score_list = [w * 3, d, l * 0]
    return sum(score_list)


print(scoring(win, draw, loss))
