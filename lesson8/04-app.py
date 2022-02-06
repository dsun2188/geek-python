class Car:
    model: str
    price: int

    def __init__(self, model, price):
        self.model = model
        self.price = price


class CarFactory:
    model = "Udia"
    common_price = 4000

    def build(self, count=1):
        cars = []

        for _ in range(count):
            cars.append(
                Car(self.model, self.common_price)
            )

        return cars


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Not enough space, current = {self.current}, needle = {self.needle}"


class CarStock:
    max_count: int
    cars: list

    def __init__(self, count=0):
        self.max_count = count
        self.cars = []

    def store(self, cars: list):
        if len(self.cars) >= self.max_count:
            raise CapacityException(len(self.cars), len(self.cars) + len(cars))
        elif len(cars) > (self.max_count - len(self.cars)):
            raise CapacityException(self.max_count, len(self.cars) + len(cars))

        self.cars.extend(cars)


class NotEnoughMoneyException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Not enough money, current = {self.current}, needle = {self.needle}"


class Customer:
    money: int

    def __init__(self, money):
        self.money = money

    def buy(self, car: Car):
        if car.price > self.money:
            raise NotEnoughMoneyException(self.money, car.price)

        self.money -= car.price


factory = CarFactory()
stock = CarStock(1)
john = Customer(100)

car_list = factory.build(4)
stock.store(car_list)

try:
    john.buy(stock.cars[1])
except NotEnoughMoneyException as exception:
    print(f"Need more {exception.needle - exception.current}")

print(john.money)