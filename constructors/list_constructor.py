import wx

import config.config as cfg
import lang.en as lang
from views.constructor import Constructor, reiterate_func


class ListCtrlPanel(Constructor):
    def __init__(self, parent, size_list=cfg.SIZE_LIST):
        super().__init__(window=1, parent=parent)
        self.columns: dict[str: int] = {}
        self.list_ctrl = wx.ListCtrl(self, size=size_list, style=wx.LC_REPORT)
        self.build_view()

    @reiterate_func
    def add_column(self, header):
        col = self.list_ctrl.GetColumnCount()
        self.list_ctrl.InsertColumn(col, lang.NAMES[header])
        self.columns.setdefault(header, col)

    @reiterate_func
    def width_column(self, header: str, width: int):
        self.list_ctrl.SetColumnWidth(col=self.columns[header], width=width)

    @reiterate_func
    def hide_column(self, header: str):
        self.width_column(header, width=0)

    @reiterate_func
    def add_row(self, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        row = self.list_ctrl.GetItemCount()
        self.list_ctrl.SetItemData(self.list_ctrl.Append(*items), row)

    @reiterate_func
    def del_row(self, row: int):
        self.list_ctrl.DeleteItem(row)

    @reiterate_func
    def get_row(self, row: int) -> tuple:
        cols = self.list_ctrl.GetColumnCount()
        return tuple(self.list_ctrl.GetItem(row, col).GetText() for col in range(cols))
