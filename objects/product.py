from pprint import pp

from objects.my_object import MyObject
from objects.detail import Detail
from objects.operation import Operation


class Product(MyObject):
    def __init__(self):
        super().__init__()
        self.size: str = None
        self._details = {}

    def add_detail(self, detail_: Detail, count: int, operation_: Operation):
        self._details.setdefault(detail.id, {'detail': detail_, 'count': count, 'operation': operation_})

    def del_detail(self, id_: int):
        del self._details[id_]

    def get_detail(self, id_: int) -> Detail:
        return self._details[id_]['detail']

    def get_count(self, id_: int) -> int:
        return self._details[id_]['count']

    def get_operation(self, id_: int) -> Operation:
        return self._details[id_]['operation']

    def print_details(self):
        pp(self._details)


if __name__ == '__main__':
    detail = Detail()
    detail.name = 'triangle'

    operation = Operation()
    operation.name = 'Kick'
    operation.cost = '100'

    product = Product()
    product.name = 'umbrella'
    product.size = '1x1'
    print(product)
    product.add_detail(detail, 10, operation)
    product.print_details()
    print(product.get_detail(detail.id))
    print(product.get_count(detail.id))
    print(product.get_operation(detail.id))
    product.del_detail(detail.id)
    product.print_details()
