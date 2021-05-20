from random import randint


class City:
    name = 'Moscow'
    street = randint(1, 10)

    def __init__(self):
        self.people = House.people
        self.house = Street.houses
        self.count_of_street = int()
        self.count_of_houses = int()

    def fill_the_city(self):
        self.street = City.street

    def pretty_table(self):
        print('Street' + '  ' + 'House' + '  ' + 'People')
        table = str(f'   {self.street}      {self.house}     {self.people}')
        return table


class Street(City):
    houses = randint(5, 20)


class House(Street):
    people = randint(1, 100)


a = City()
print(a.pretty_table())
