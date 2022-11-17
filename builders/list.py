from abc import abstractmethod

import wx

from builders.panel import BPanel
from support_tools.funcs import reiterate_func_with_one_arg, reiterate_func_with_two_args, reiterate_get_func_with_one_arg


class BList(BPanel):
    def __init__(self, parent, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL):
        super().__init__(parent=parent, size=size, style=style)
        self.columns = {}
        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)

    @abstractmethod
    def create_widgets(self):
        pass

    @abstractmethod
    def build_view(self):
        pass

    def set_size_list(self, width: int, height: int):
        self.list_ctrl.SetSize((width, height))
        self.list_ctrl.SetMinSize((width, height))

    @reiterate_func_with_one_arg
    def add_column(self, header: str):
        col = self.list_ctrl.GetColumnCount()
        self.list_ctrl.InsertColumn(col, header)
        self.columns.setdefault(header, col)

    @reiterate_func_with_two_args
    def set_width_column(self, header: str, width: int):
        self.list_ctrl.SetColumnWidth(col=self.columns[header], width=width)

    def set_width_group_columns(self, *headers, width: int):
        for header in headers:
            self.set_width_column(header, width)

    @reiterate_func_with_one_arg
    def hide_column(self, header: str):
        width = 0  # Decorator reiterate_func_with_two_args get error because width argument, which transferred how key value in the function of
        # the set_width_column
        self.set_width_column(header, width)

    def add_row(self, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        row = self.list_ctrl.GetItemCount()
        self.list_ctrl.SetItemData(self.list_ctrl.Append(items), row)

    @reiterate_get_func_with_one_arg
    def get_row(self, row: int) -> tuple | tuple[tuple] | None | tuple[None]:
        cols = self.list_ctrl.GetColumnCount()
        ret = tuple(self.list_ctrl.GetItem(row, col).GetText() for col in range(cols))
        if len(ret) == 1 and ret[0] == '':
            ret = None
        return ret

    def set_row(self, row: int, *items: str, skip_col: tuple = ()):
        cols = [num for num in self.columns.values() if num not in skip_col]
        assert len(cols) == len(items)
        for col, item in zip(cols, items):
            self.list_ctrl.SetItem(row, col, item[0] if type(item) is list else item)

    @reiterate_func_with_one_arg
    def del_row(self, row: int):
        self.list_ctrl.DeleteItem(row)



if __name__ == '__main__':
    ...
