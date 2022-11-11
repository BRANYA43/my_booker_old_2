from views.patterns.list import PVList
from funcs_support import test_panel


class VList(PVList):
    def __init__(self, parent):
        super().__init__(parent=parent, name='product')


if __name__ == "__main__":
    test_panel(VList)
