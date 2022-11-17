import unittest

import wx

from builders.info import InfoBuilder


class TestInfoBuilder(unittest.TestCase):
    def setUp(self):
        class TestFrame(wx.Frame, InfoBuilder):
            def __init__(self):
                wx.Frame.__init__(self, None)
                InfoBuilder.__init__(self, parent=self)

            def create_widgets(self):
                pass

            def build_view(self):
                pass

        self.app = wx.App()
        self.b_info = TestFrame()

    def test_create_static_text(self):
        names =['full_name', 'payment', 'rate']
        self.b_info.create_static_text(*names, add=True)
        for name in names:
            self.assertIn(name, self.b_info.labels)

    def test_set_labels(self):
        values = ['first name second name', 'hourly work', '100']
        self.b_info.create_static_text('full_name', 'payment', 'rate', add=True)
        self.b_info.set_labels(*values)
        static_texts = self.b_info.get_static_text('full_name', 'payment', 'rate')
        for static_text, value in zip(static_texts, values):
            self.assertEqual(value, static_text.GetLabel())


if __name__ == '__main__':
    unittest.main()