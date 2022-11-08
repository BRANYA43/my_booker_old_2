import wx

import config.config as cfg
import lang.en as lang
from constructors.panel_constructor import PanelConstructor
from funcs_support import reiterate_func


class ListConstructor(PanelConstructor):
    def __init__(self, parent, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL):
        super().__init__(parent=parent, size=size, style=style)
        self.columns = {}
        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)

    def set_size_list(self, width: int, height: int):
        self.list_ctrl.SetMinSize((width, height))

    @reiterate_func
    def add_column(self, header: str):
        col = self.list_ctrl.GetColumnCount()
        self.list_ctrl.InsertColumn(col, lang.NAMES[header])
        self.columns.setdefault(header, col)

    @reiterate_func
    def set_width_column(self, header: str, width: int):
        self.list_ctrl.SetColumnWidth(col=self.columns[header], width=width)

    @reiterate_func
    def hide_column(self, header: str):
        self.set_width_column(header, width=0)

    def add_row(self, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        row = self.list_ctrl.GetItemCount()
        self.list_ctrl.SetItemData(self.list_ctrl.Append(items), row)

    @reiterate_func
    def del_row(self, row: int):
        self.list_ctrl.DeleteItem(row)

    @reiterate_func
    def get_row(self, row: int) -> tuple:
        cols = self.list_ctrl.GetColumnCount()
        return tuple(self.list_ctrl.GetItem(row, col).GetText() for col in range(cols))

    def set_row(self, row: int, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        for col, item in items:
            self.list_ctrl.SetItem(row, col, item)

if __name__ == '__main__':
    ...
