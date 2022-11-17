import unittest

import wx

from builders.notebook import BNotebook


class TestBNotebook(unittest.TestCase):
    def setUp(self):
        class TestFrame(BNotebook):
            def __init__(self):
                BNotebook.__init__(self, parent=None)

            def create_widgets(self):
                pass

            def build_view(self):
                pass

        self.app = wx.App()
        self.b_notebook = TestFrame()

    def test_add_page(self):
        panel_ = wx.Panel(self.b_notebook.notebook)
        self.b_notebook.add_page('Home', panel_)
        panel = self.b_notebook.pages.get('Home')
        self.assertIsNotNone(panel)
        self.assertEqual(wx.Panel, type(panel))
        self.assertEqual(wx.Panel, type(self.b_notebook.notebook.GetCurrentPage()))


if __name__ == '__main__':
    unittest.main()
