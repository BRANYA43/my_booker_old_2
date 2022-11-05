import wx

import config.config as cfg
import lang.en as lang
from objects.constructor import Constructor


class ListCtrlPanel(Constructor):
    def __init__(self, parent, size_list=cfg.SIZE_LIST):
        super().__init__(window=1, parent=parent)
        self.columns: dict[str: int] = {}
        self.list_ctrl = wx.ListCtrl(self, size=size_list, style=wx.LC_REPORT)
        self.build_view()

    def add_column(self, *headers):
        for col, header in enumerate(headers):
            self.list_ctrl.InsertColumn(col, lang.NAMES[header])
            self.columns.setdefault(header, col)

    def width_column(self, width: int, *headers):
        for header in headers:
            self.list_ctrl.SetColumnWidth(col=self.columns[header], width=width)

    def hide_column(self, *headers):
        self.width_column(width=0, *headers)

    def add_row(self, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        row = self.list_ctrl.GetItemCount()
        self.list_ctrl.SetItemData(self.list_ctrl.Append(items), row)

    def del_row(self, row: int):
        self.list_ctrl.DeleteItem(row)

    def get_row(self, row: int) -> tuple:
        cols = self.list_ctrl.GetColumnCount()
        return tuple(self.list_ctrl.GetItem(row, col).GetText() for col in range(cols))
