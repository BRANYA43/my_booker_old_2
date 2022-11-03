from decimal import Decimal

from my_object import MyObject


class Laborer(MyObject):
    def __init__(self):
        super().__init__()
        self.payment: str = None
        self._rate = Decimal('0')

    @property
    def rate(self) -> Decimal:
        return self._rate

    @rate.setter
    def rate(self, rate: str):
        self._rate = Decimal(rate)


if __name__ == '__main__':
    for i in range(10):
        laborer = Laborer()
        laborer.name = f'L-{i}'
        print(laborer)
        laborer.rate = f'{100 + i * i}'
        print(laborer.rate)
