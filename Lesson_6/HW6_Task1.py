coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC',)


def make_dict():
    d = {coin[i]: code[i] for i in range(len(coin))}
    print(d)


make_dict()
# Читерский вариант:
s = dict(zip(coin, code))
print(s)
