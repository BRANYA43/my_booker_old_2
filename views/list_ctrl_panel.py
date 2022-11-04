import wx

import config.config as cfg
import lang.en as lang


class ListCtrlPanel(wx.Panel):
    def __init__(self, parent, size_list=cfg.SIZE_LIST):
        super().__init__(parent=parent)
        self.btns: dict[str: wx.Button] = {}
        self.columns: dict[str: int] = {}
        self.list_ctrl = wx.ListCtrl(self, size=size_list, style=wx.LC_REPORT)
        self.build_panel()

    def add_button(self, *labels):
        for label in labels:
            self.btns.setdefault(label, wx.Button(self, label=lang.NAMES[label]))

    def enable_button(self, *labels):
        for label in labels:
            self.btns[label].Enable(True)

    def disable_button(self, *labels):
        for label in labels:
            self.btns[label].Enable(False)

    def bind_button(self, func, label):
        button = self.btns[label]
        self.Bind(wx.EVT_BUTTON, func, button)

    def add_column(self, *headers):
        for col, header in enumerate(headers):
            self.list_ctrl.InsertColumn(col, lang.NAMES[header])
            self.columns.setdefault(header, col)

    def hide_column(self, *headers):
        self.width_column(width=0, *headers)

    def width_column(self, width: int, *headers):
        for header in headers:
            self.list_ctrl.SetColumnWidth(col=self.columns[header], width=width)

    def get_row(self, row: int) -> tuple:
        cols = self.list_ctrl.GetColumnCount()
        return tuple(self.list_ctrl.GetItem(row, col).GetText() for col in range(cols))

    def add_row(self, *items):
        assert len(items) == self.list_ctrl.GetColumnCount()
        row = self.list_ctrl.GetItemCount()
        self.list_ctrl.SetItemData(self.list_ctrl.Append(items), row)

    def del_row(self, row: int):
        self.list_ctrl.DeleteItem(row)

    def build_panel(self):
        raise NotImplemented
