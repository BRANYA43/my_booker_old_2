import unittest

import wx

from builders.list import ListBuilder


class TestListBuilder(unittest.TestCase):
    def setUp(self):
        class TestFrame(wx.Frame, ListBuilder):
            def __init__(self):
                wx.Frame.__init__(self, None)
                ListBuilder.__init__(self, parent=self)

            def create_widgets(self):
                pass

            def build_view(self):
                pass

        self.app = wx.App()
        self.b_list = TestFrame()

    def test_set_size_list(self):
        self.b_list.set_size_list(width=100, height=100)
        self.assertEqual(wx.Size(100, 100), self.b_list.list_ctrl.GetSize())

    def test_add_column(self):
        # Check for creation of a column
        self.b_list.add_column('header')
        self.assertIn('header', self.b_list.columns.keys())
        self.assertIsNotNone(self.b_list.columns.get('header'))
        self.assertEqual(0, self.b_list.columns['header'])

        self.assertEqual(1, self.b_list.list_ctrl.GetColumnCount())
        self.assertEqual('header', self.b_list.list_ctrl.GetColumn(0).GetText())
        self.b_list.list_ctrl.DeleteColumn(0)
        del self.b_list.columns['header']

        # Check for creation of some columns
        headers = ['h-0', 'h-1', 'h-2']
        self.b_list.add_column(*headers)
        for i, header in enumerate(headers):
            self.assertIn(header, self.b_list.columns.keys())
            self.assertIsNotNone(self.b_list.columns.get(header))
            self.assertEqual(i, self.b_list.columns[header])

        self.assertEqual(len(headers), self.b_list.list_ctrl.GetColumnCount())
        for i, header in enumerate(headers):
            self.assertEqual(header, self.b_list.list_ctrl.GetColumn(i).GetText())

    def test_set_width_column(self):
        self.b_list.add_column('header')
        self.b_list.set_width_column('header', 100)
        self.assertEqual(100, self.b_list.list_ctrl.GetColumn(0).GetWidth())
        self.b_list.list_ctrl.DeleteColumn(0)
        del self.b_list.columns['header']

        headers = ['h-0', 'h-1', 'h-2']
        widths = [100, 50, 200]
        self.b_list.add_column(*headers)
        self.b_list.set_width_column('h-0', 100, 'h-1', 50, 'h-2', 200)
        for i, width in enumerate(widths):
            self.assertEqual(width, self.b_list.list_ctrl.GetColumn(i).GetWidth())

    def test_set_width_group_columns(self):
        headers = ['h-0', 'h-1', 'h-2']
        self.b_list.add_column(*headers)
        self.b_list.set_width_group_columns(*headers, width=300)
        for i, header in enumerate(headers):
            self.assertEqual(300, self.b_list.list_ctrl.GetColumn(i).GetWidth())

    def test_hide_column(self):
        self.b_list.add_column('header')
        self.b_list.hide_column('header')
        self.assertEqual(0, self.b_list.list_ctrl.GetColumn(0).GetWidth())
        self.b_list.list_ctrl.DeleteColumn(0)
        del self.b_list.columns['header']

        headers = ['h-0', 'h-1', 'h-2']
        self.b_list.add_column(*headers)
        self.b_list.hide_column(*headers)
        for i, header in enumerate(headers):
            self.assertEqual(0, self.b_list.list_ctrl.GetColumn(i).GetWidth())

    def test_add_row(self):
        self.b_list.add_column('header')
        self.b_list.add_row('header_name')
        self.assertEqual('header_name', self.b_list.list_ctrl.GetItem(0).GetText())
        self.b_list.list_ctrl.DeleteItem(0)
        self.b_list.list_ctrl.DeleteColumn(0)
        del self.b_list.columns['header']

        self.b_list.add_column('name', 'id', 'date')
        self.b_list.add_row('bob', 1000, 25)
        self.assertEqual('bob', self.b_list.list_ctrl.GetItem(0, 0).GetText())
        self.assertEqual('1000', self.b_list.list_ctrl.GetItem(0, 1).GetText())
        self.assertEqual('25', self.b_list.list_ctrl.GetItem(0, 2).GetText())

    def test_get_row(self):
        self.b_list.add_column('name', 'id')
        self.b_list.add_row('bob', 1000)
        row_data = self.b_list.get_row(0)
        self.assertIs(tuple, type(row_data))
        self.assertIn('bob', row_data)
        self.assertIn('1000', row_data)

        for i in range(1, 4):
            name = f'b-{i}'
            id_ = 1000 + i
            self.b_list.add_row(name, id_)
            row_data = self.b_list.get_row(i)
            self.assertIs(tuple, type(row_data))
            self.assertIn(name, row_data)
            self.assertIn(str(id_), row_data)

        rows_data = self.b_list.get_row(1, 3, 0)
        self.assertIs(tuple, type(rows_data))
        self.assertIn('b-1', rows_data[0])
        self.assertIn('b-3', rows_data[1])
        self.assertIn('bob', rows_data[2])
        self.assertIn('1001', rows_data[0])
        self.assertIn('1003', rows_data[1])
        self.assertIn('1000', rows_data[2])

    def test_set_row(self):
        self.b_list.add_column('name', 'id')
        self.b_list.add_row('bob', 1000)
        self.b_list.add_row('bib', 1001)
        self.b_list.set_row(0, 'gulya', skip_col=(1,))
        row_data = self.b_list.get_row(0, 1)
        self.assertIn('gulya', row_data[0])
        self.assertIn('1000', row_data[0])
        self.assertIn('bib', row_data[1])
        self.assertIn('1001', row_data[1])
        self.b_list.set_row(1, 'nik', '200')
        row_data = self.b_list.get_row(0, 1)
        self.assertIn('gulya', row_data[0])
        self.assertIn('1000', row_data[0])
        self.assertIn('nik', row_data[1])
        self.assertIn('200', row_data[1])

    def test_del_row(self):
        self.b_list.add_column('header')
        self.b_list.add_row('bob')
        self.b_list.del_row(0)
        row_data = self.b_list.get_row(0)
        self.assertIsNone(row_data)


if __name__ == '__main__':
    unittest.main()
