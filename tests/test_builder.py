import unittest

import wx

from builders.builder import Builder


class TestBuilder(unittest.TestCase):
    def setUp(self):
        class MetaFrame(type(wx.Frame), type(Builder)):
            pass

        class TestFrame(wx.Frame, Builder, metaclass=MetaFrame):
            def __init__(self):
                wx.Frame.__init__(self, None)
                Builder.__init__(self)

            def create_widgets(self):
                pass

            def build_view(self):
                pass

        self.app = wx.App()
        self.builder = TestFrame()

    def test_add_widget(self):
        self.builder.add_widget('btn', 'save', wx.Button(self.builder))
        self.assertIsNotNone(self.builder.widgets.get('btn'))
        self.assertIsNotNone(self.builder.widgets['btn'].get('save'))
        self.assertEqual(wx.Button, type(self.builder.widgets['btn']['save']))

    def test_create_widget(self):
        for type_, class_ in self.builder.widget_classes.items():
            self.builder.create_widget(type_, 'widget', pos=(100, 100))
            widget = self.builder.widgets[type_]['widget']
            self.assertEqual(class_, type(widget))
            self.assertEqual((100, 100), widget.GetPosition())
        self.builder.create_widget('btn', 'save')
        self.assertIsNotNone(self.builder.widgets['btn']['save'])

    def test_get_widget(self):
        self.builder.create_widget('btn', 'save')
        gotten_widget = self.builder.get_widget('btn', 'save')
        self.assertIs(wx.Button, type(gotten_widget))

        for i in range(5):
            self.builder.create_widget('btn', f'b-{i}')
        gotten_tuple_widgets = self.builder.get_widget('btn', 'b-0', 'btn', 'b-1', 'btn', 'b-2', 'btn', 'b-3', 'btn', 'b-4')
        self.assertIs(tuple, type(gotten_tuple_widgets))
        for btn in gotten_tuple_widgets:
            self.assertEqual(wx.Button, type(btn))

    def test_enable_button(self):
        ...

    def test_disable_button(self):
        ...

    def test_bind_widget(self):
        ...

    def test_create_btn(self):
        # 1 Checks for creation of a button with default arguments
        self.builder.create_btn('save')
        btn = self.builder.get_widget('btn', 'save')
        self.assertEqual(wx.Button, type(btn))
        self.assertEqual(self.builder.NOT_NAMED, btn.GetLabel())
        self.assertEqual((0, 0), btn.GetPosition())

        # 2 Checks for creation of a button with set arguments
        self.builder.create_btn('add', label='Button', pos=(10, 10), width=100, height=50)
        btn = self.builder.get_widget('btn', 'add')
        self.assertEqual(wx.Button, type(btn))
        self.assertEqual('Button', btn.GetLabel())
        self.assertEqual((10, 10), btn.GetPosition())
        self.assertEqual(wx.Size(100, 50), btn.GetSize())

        # 3 Checks for creation of a button with set flag auto_name_label
        self.builder.create_btn('delete', auto_name_label=True)
        btn = self.builder.get_widget('btn', 'delete')
        self.assertEqual(wx.Button, type(btn))
        self.assertEqual('delete', btn.GetLabel())
        self.assertEqual((0, 0), btn.GetPosition())

        # 4 Checks for creation of a group buttons with default arguments
        self.builder.create_btn('b-0', 'b-1', 'b-2', 'b-3', 'b-4')
        btns = self.builder.get_widget('btn', 'b-0', 'btn', 'b-1', 'btn', 'b-2', 'btn', 'b-3', 'btn', 'b-4')
        for btn in btns:
            self.assertEqual(wx.Button, type(btn))
            self.assertEqual(self.builder.NOT_NAMED, btn.GetLabel())
            self.assertEqual((0, 0), btn.GetPosition())

        # 5 Checks for creation of a group buttons with set arguments
        self.builder.create_btn('b-5', 'b-6', 'b-7', 'b-8', 'b-9', label='Button', pos=(10, 10), width=100, height=50)
        btns = self.builder.get_widget('btn', 'b-5', 'btn', 'b-6', 'btn', 'b-7', 'btn', 'b-8', 'btn', 'b-9')
        for btn in btns:
            self.assertEqual(wx.Button, type(btn))
            self.assertEqual('Button', btn.GetLabel())
            self.assertEqual((10, 10), btn.GetPosition())
            self.assertEqual(wx.Size(100, 50), btn.GetSize())

        # 6 Check for creation of a group buttons with set flag auto_name_label
        names = ['edit', 'ok', 'no']
        self.builder.create_btn(*names, auto_name_label=True)
        btns = self.builder.get_widget('btn', 'edit', 'btn', 'ok', 'btn', 'no')
        for btn, name in zip(btns, names):
            self.assertEqual(wx.Button, type(btn))
            self.assertEqual(name, btn.GetLabel())
            self.assertEqual((0, 0), btn.GetPosition())

    def test_create_static_text(self):
        # 1 Checks for creation of static text with default arguments
        self.builder.create_static_text('name')
        static_text = self.builder.get_widget('static_text', 'name')
        self.assertEqual(wx.StaticText, type(static_text))
        self.assertEqual(self.builder.NOT_NAMED, static_text.GetLabel())
        self.assertEqual((0, 0), static_text.GetPosition())

        # 2 Checks for creation of a static text with set arguments
        self.builder.create_static_text('test', label='test_label', pos=(10, 10), width=100, height=50)
        static_text = self.builder.get_widget('static_text', 'test')
        self.assertEqual(wx.StaticText, type(static_text))
        self.assertEqual('test_label', static_text.GetLabel())
        self.assertEqual((10, 10), static_text.GetPosition())
        self.assertEqual(wx.Size(100, 50), static_text.GetSize())

        # 3 Checks for creation of a static text with flag colon
        self.builder.create_static_text('full_name', colon=True)
        static_text = self.builder.get_widget('static_text', 'full_name')
        self.assertEqual(wx.StaticText, type(static_text))
        self.assertEqual(self.builder.NOT_NAMED + ':', static_text.GetLabel())
        self.assertEqual((0, 0), static_text.GetPosition())

        # 4 Checks for creation of a static text with flag auto_name_label
        self.builder.create_static_text('rate', auto_name_label=True)
        static_text = self.builder.get_widget('static_text', 'rate')
        self.assertEqual(wx.StaticText, type(static_text))
        self.assertEqual('rate', static_text.GetLabel())
        self.assertEqual((0, 0), static_text.GetPosition())

        # 5 Checks for creation of a static text with flags colon and auto_name_label
        self.builder.create_static_text('salary', auto_name_label=True, colon=True)
        static_text = self.builder.get_widget('static_text', 'salary')
        self.assertEqual(wx.StaticText, type(static_text))
        self.assertEqual('salary:', static_text.GetLabel())
        self.assertEqual((0, 0), static_text.GetPosition())

        # 6 Checks for creation a group static text with default arguments
        self.builder.create_static_text('st-0', 'st-1', 'st-2', 'st-3', 'st-4')
        static_texts = self.builder.get_widget('static_text', 'st-0', 'static_text', 'st-1', 'static_text', 'st-2', 'static_text', 'st-3',
                                               'static_text', 'st-4')
        for static_text in static_texts:
            self.assertEqual(wx.StaticText, type(static_text))
            self.assertEqual(self.builder.NOT_NAMED, static_text.GetLabel())
            self.assertEqual((0, 0), static_text.GetPosition())

        # 7 Checks for creation a group static text with set arguments
        self.builder.create_static_text('st-5', 'st-6', 'st-7', 'st-8', 'st-9', label='test_label_group', pos=(10, 10), width=100, height=50)
        static_texts = self.builder.get_widget('static_text', 'st-5', 'static_text', 'st-6', 'static_text', 'st-7', 'static_text', 'st-8',
                                               'static_text', 'st-9')
        for static_text in static_texts:
            self.assertEqual(wx.StaticText, type(static_text))
            self.assertEqual('test_label_group', static_text.GetLabel())
            self.assertEqual((10, 10), static_text.GetPosition())
            self.assertEqual(wx.Size(100, 50), static_text.GetSize())

        # 8 Check for creation a group static text with set flag colon
        names = ['cat', 'dog', 'cow']
        self.builder.create_static_text(*names, colon=True)
        static_texts = self.builder.get_widget('static_text', 'cat', 'static_text', 'dog', 'static_text', 'cow')
        for static_text in static_texts:
            self.assertEqual(wx.StaticText, type(static_text))
            self.assertEqual(self.builder.NOT_NAMED + ':', static_text.GetLabel())
            self.assertEqual((0, 0), static_text.GetPosition())

        # 9 Check for creation a group static text with set flag auto_name_label
        names = ['fox', 'pig', 'rick']
        self.builder.create_static_text(*names, auto_name_label=True)
        static_texts = self.builder.get_widget('static_text', 'fox', 'static_text', 'pig', 'static_text', 'rick')
        for static_text, name in zip(static_texts, names):
            self.assertEqual(wx.StaticText, type(static_text))
            self.assertEqual(name, static_text.GetLabel())
            self.assertEqual((0, 0), static_text.GetPosition())

        # 10 Checks fot creation a group static text with set flags colon and auto_name_label
        names = ['morty', 'city', 'iron']
        self.builder.create_static_text(*names, auto_name_label=True, colon=True)
        static_texts = self.builder.get_widget('static_text', 'morty', 'static_text', 'city', 'static_text', 'iron')
        for static_text, name in zip(static_texts, names):
            self.assertEqual(wx.StaticText, type(static_text))
            self.assertEqual(name + ':', static_text.GetLabel())
            self.assertEqual((0, 0), static_text.GetPosition())

    def test_create_text_ctrl(self):
        # 1 Checks for creation of a text ctrl with default arguments
        self.builder.create_text_ctrl('entry_field')
        text_ctrl = self.builder.get_widget('text_ctrl', 'entry_field')
        self.assertEqual(wx.TextCtrl, type(text_ctrl))
        self.assertEqual(wx.EmptyString, text_ctrl.GetValue())
        self.assertEqual((0, 0), text_ctrl.GetPosition())

        # 2 Checks for creation of a text ctrl with set arguments
        self.builder.create_text_ctrl('entry_field_', value='empty field', pos=(10, 10), width=100, height=50)
        text_ctrl = self.builder.get_widget('text_ctrl', 'entry_field_')
        self.assertEqual(wx.TextCtrl, type(text_ctrl))
        self.assertEqual('empty field', text_ctrl.GetValue())
        self.assertEqual((10, 10), text_ctrl.GetPosition())
        self.assertEqual(wx.Size(100, 50), text_ctrl.GetSize())

        # 3 Checks for creation of a group text ctrls with default arguments
        self.builder.create_text_ctrl('tc-0', 'tc-1', 'tc-2', 'tc-3', 'tc-4')
        text_ctrls = self.builder.get_widget('text_ctrl', 'tc-0', 'text_ctrl', 'tc-1', 'text_ctrl', 'tc-2', 'text_ctrl', 'tc-3', 'text_ctrl', 'tc-4')
        for text_ctrl in text_ctrls:
            self.assertEqual(wx.TextCtrl, type(text_ctrl))
            self.assertEqual(wx.EmptyString, text_ctrl.GetValue())
            self.assertEqual((0, 0), text_ctrl.GetPosition())

        # 4 Checks for creation of a group text ctrls with set arguments
        self.builder.create_text_ctrl('tc-5', 'tc-6', 'tc-7', 'tc-8', 'tc-9', value='not empty field', pos=(10, 10), width=100, height=50)
        text_ctrls = self.builder.get_widget('text_ctrl', 'tc-5', 'text_ctrl', 'tc-6', 'text_ctrl', 'tc-7', 'text_ctrl', 'tc-8', 'text_ctrl', 'tc-9')
        for text_ctrl in text_ctrls:
            self.assertEqual(wx.TextCtrl, type(text_ctrl))
            self.assertEqual('not empty field', text_ctrl.GetValue())
            self.assertEqual((10, 10), text_ctrl.GetPosition())
            self.assertEqual(wx.Size(100, 50), text_ctrl.GetSize())

    def test_create_combobox(self):
        # 1 Checks for creation of a combobox with default arguments and empty list
        self.builder.create_combobox('list', [])
        combobox = self.builder.get_widget('combobox', 'list')
        self.assertEqual(wx.ComboBox, type(combobox))
        self.assertEqual(wx.EmptyString, combobox.GetValue())
        self.assertEqual((0, 0), combobox.GetPosition())

        # 2 Checks for creation of a combobox with default arguments and not empty list
        self.builder.create_combobox('list_', ['1', '2', '3'])
        combobox = self.builder.get_widget('combobox', 'list_')
        self.assertEqual(wx.ComboBox, type(combobox))
        self.assertEqual('1', combobox.GetValue())
        self.assertEqual((0, 0), combobox.GetPosition())

        # 3 Checks for creation of a combobox with set arguments and empty list
        self.builder.create_combobox('item_list', [], value='item', pos=(10, 10), width=100)
        combobox = self.builder.get_widget('combobox', 'item_list')
        self.assertEqual(wx.ComboBox, type(combobox))
        self.assertEqual('item', combobox.GetValue())
        self.assertEqual((10, 10), combobox.GetPosition())
        self.assertEqual(wx.Size(100, -1)[0], combobox.GetSize()[0])

        # 4 Checks for creation of a combobox with set arguments and not empty list
        self.builder.create_combobox('item_list_', ['1', '2', '3'], value='item', pos=(10, 10), width=100)
        combobox = self.builder.get_widget('combobox', 'item_list_')
        self.assertEqual(wx.ComboBox, type(combobox))
        self.assertEqual('item', combobox.GetValue())
        self.assertEqual((10, 10), combobox.GetPosition())
        self.assertEqual(wx.Size(100, -1)[0], combobox.GetSize()[0])

        # 5 Checks for creation of a group combobox with default arguments and empty list
        self.builder.create_combobox('elem_list', [], 'num_list', [], 'name_list', [])
        comboboxes = self.builder.get_widget('combobox', 'elem_list', 'combobox', 'num_list', 'combobox', 'name_list')
        for combobox in comboboxes:
            self.assertEqual(wx.ComboBox, type(combobox))
            self.assertEqual(wx.EmptyString, combobox.GetValue())
            self.assertEqual((0, 0), combobox.GetPosition())

        # 6 Checks for creation of a group combobox with set arguments and not empty list
        some_list = [['e-1', 'e-2', 'e-3'], ['1', '2', '3'], ['name-1', 'name-2', 'name-3']]
        self.builder.create_combobox('elem_list_', some_list[0], 'num_list_', some_list[1], 'name_list_', some_list[2])
        comboboxes = self.builder.get_widget('combobox', 'elem_list_', 'combobox', 'num_list_', 'combobox', 'name_list_')
        for combobox, list_ in zip(comboboxes, some_list):
            self.assertEqual(type(combobox), wx.ComboBox)
            self.assertEqual(list_[0], combobox.GetValue())
            self.assertEqual((0, 0), combobox.GetPosition())

        # 7
        # 8

    def test_bind_btn(self):
        ...

    def test_get_btn(self):
        self.builder.create_btn('save')
        btn = self.builder.get_btn('save')
        self.assertEqual(type(btn), wx.Button)

        for i in range(5):
            self.builder.create_btn(f'b-{i}')
        btns = self.builder.get_btn('b-0', 'b-1', 'b-2', 'b-3', 'b-4')
        self.assertEqual(type(btns), tuple)
        for btn_ in btns:
            self.assertEqual(type(btn_), wx.Button)

    def test_get_static_text(self):
        self.builder.create_static_text('label')
        static_text = self.builder.get_static_text('label')
        self.assertEqual(type(static_text), wx.StaticText)

        for i in range(5):
            self.builder.create_static_text(f'st-{i}')
        static_texts = self.builder.get_static_text('st-0', 'st-1', 'st-2', 'st-3', 'st-4')
        self.assertEqual(type(static_texts), tuple)
        for static_text_ in static_texts:
            self.assertEqual(type(static_text_), wx.StaticText)

    def test_get_text_ctrl(self):
        self.builder.create_text_ctrl('entry_field')
        text_ctrl = self.builder.get_text_ctrl('entry_field')
        self.assertEqual(type(text_ctrl), wx.TextCtrl)

        for i in range(5):
            self.builder.create_text_ctrl(f'tc-{i}')
        text_ctrls = self.builder.get_text_ctrl('tc-0', 'tc-1', 'tc-2', 'tc-3', 'tc-4')
        self.assertEqual(type(text_ctrls), tuple)
        for text_ctrl_ in text_ctrls:
            self.assertEqual(type(text_ctrl_), wx.TextCtrl)

    def test_get_combobox(self):
        self.builder.create_combobox('list', [])
        combobox = self.builder.get_combobox('list')
        self.assertEqual(type(combobox), wx.ComboBox)

        for i in range(5):
            self.builder.create_combobox(f'cb-{i}', [])
        comboboxes = self.builder.get_combobox('cb-0', 'cb-1', 'cb-2', 'cb-3', 'cb-4')
        self.assertEqual(type(comboboxes), tuple)
        for combobox_ in comboboxes:
            self.assertEqual(type(combobox_), wx.ComboBox)

    def test_get_value(self):
        self.builder.create_text_ctrl('name', value='value')
        self.assertEqual('value', self.builder.get_value('text_ctrl', 'name'))

    def test_set_value(self):
        self.builder.create_text_ctrl('name', value='value')
        self.builder.set_value('text_ctrl', 'name', 'BOB')
        self.assertEqual('BOB', self.builder.get_value('text_ctrl', 'name'))

    def test_get_label(self):
        self.builder.create_static_text('name', label='label')
        self.assertEqual('label', self.builder.get_label('static_text', 'name'))

    def test_set_label(self):
        self.builder.create_static_text('name', label='label')
        self.builder.set_label('static_text', 'name', 'button')
        self.assertEqual('button', self.builder.get_label('static_text', 'name'))


if __name__ == '__main__':
    unittest.main()
