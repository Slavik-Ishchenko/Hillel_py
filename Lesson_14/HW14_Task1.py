import csv


class Product:
    def __init__(self, name_of_product, type_of_product, price_of_product):
        self.name = name_of_product
        self.type = type_of_product
        self.price = price_of_product

    def output(self):
        print(f'{self.type}: {self.name}, цена: {self.price}')

    def get_prices(self):
        return self.price

    def __repr__(self):
        """Превращает self.products в нормальный вид"""
        if self.type == 'coffee':
            self.type = 'Кофе'
        if self.type == 'tea':
            self.type = 'Чай'
        if self.type == 'bakery':
            self.type = 'Хлеб'
        return f'{self.type}: {self.name}, цена: {self.price}'


class Store:
    def __init__(self):
        self.balance = 0.00
        self.products = []

    def product_lst_import(self):
        with open('inventory.csv') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                self.products.append(Product(row['Product'], row['Type'], row['Price']))
        return self.products*5

    def all_assort(self):
        """Выводит все продукты"""
        for prod in self.products:
            print(prod)

    def need_type(self, type_inp):
        for prod in self.products:
            if type_inp == prod.type:
                prod.output()

    def prices(self):
        """Возвращает итоговую сумму оставшихся продуктов в меню"""
        bill = 0
        for prod in self.products:
            bill += int(prod.get_prices())
        return bill

    def sale(self, name_inp):
        for prod in self.products:
            if name_inp == prod.name:
                self.balance += int(prod.get_prices())
                return prod

    def proceed(self):
        return self.balance

    def dell_prod(self, product_inp):
        for prod in self.products:
            if product_inp == prod.name:
                self.products.pop(self.products.index(prod))


shop = Store()
shop.product_lst_import()
shop.sale('Earl Grey')
shop.sale('Хлеб')
shop.dell_prod('Earl Grey')
shop.dell_prod('Хлеб')
shop.sale('Зеленый чай с жасмином')
shop.dell_prod('Зеленый чай с жасмином')
shop.all_assort()
shop.proceed()
shop.prices()
print('Итоговый счет составил: ', shop.proceed())
print('Выручка составила: ', shop.proceed())
print('Баланс составил: ', shop.proceed()+shop.prices())
