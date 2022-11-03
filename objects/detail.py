from my_object import MyObject


class Detail(MyObject):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    for i in range(10):
        detail = Detail()
        detail.name = f'd-{i}'
        print(detail)
