from views.pattern.list import PVList
from funcs_support import test_panel


class VList(PVList):
    def __init__(self, parent):
        super().__init__(parent=parent, name='laborer')


if __name__ == '__main__':
    test_panel(VList)
