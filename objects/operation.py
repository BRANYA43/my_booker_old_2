from decimal import Decimal

from my_object import MyObject


class Operation(MyObject):
    def __init__(self):
        super().__init__()
        self._cost = Decimal('0')

    @property
    def cost(self) -> Decimal:
        return self._cost

    @cost.setter
    def cost(self, cost: str):
        self._cost = Decimal(cost)


if __name__ == '__main__':
    for i in range(10):
        operation = Operation()
        operation.name = f'Op-{i}'
        operation.cost = f'{100 + i * i}'
        print(operation)
        print(operation.cost)
