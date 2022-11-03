from id_ import ID


class MyObject:
    def __init__(self):
        self._id = ID()
        self.name: str = None

    @property
    def id(self) -> int:
        return self._id.get_id()

    def __repr__(self):
        return f'Name: {self.name} ID:{self._id.get_id()}'


if __name__ == '__main__':
    for i in range(10):
        my_object = MyObject()
        print(my_object)
        print(my_object.id)
        print(my_object.name)
