class ID:
    next_id = 1000

    def __init__(self):
        self._id = None
        self._set_id()
        self._enlarge_next_id()

    def get_id(self) -> int:
        return self._id

    def _set_id(self):
        self._id = self.next_id

    @classmethod
    def _enlarge_next_id(cls):
        cls.next_id += 1

    def __repr__(self):
        return f'Object ID: id={self._id}'


if __name__ == '__main__':
    for i in range(10):
        id_ = ID()
        print(id_)
