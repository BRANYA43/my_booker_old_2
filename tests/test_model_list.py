import unittest

import wx

from objects.my_object import MyObject
from models.list import ListModel


class TestListModel(unittest.TestCase):
    def setUp(self):
        self.model = ListModel()

    def test_set_none_selected_attrs(self):
        self.model.selected_row = 1
        self.model.selected_object = MyObject()
        self.model.selected_object_id = 1000
        self.model.set_none_selected_attrs()
        self.assertIsNone(self.model.selected_row)
        self.assertIsNone(self.model.selected_object)
        self.assertIsNone(self.model.selected_object_id)

    def test_set_attrs_object(self):
        my_object = MyObject()
        self.model.set_attrs_object(my_object, name='some_name')
        self.assertEqual('some_name', my_object.name)

    def test_add_object(self):
        my_object = MyObject()
        self.model.add_object(my_object)
        self.assertEqual(1, len(self.model.objects))
        self.assertIsNotNone(self.model.objects.get(my_object.id))
        self.assertEqual(MyObject, type(my_object))

    def test_create_object(self):
        self.model.create_object(MyObject, name='some_name')
        self.assertEqual(1, len(self.model.objects))

    def test_get_object(self):
        my_object = MyObject()
        self.model.add_object(my_object)
        gotten_object_ = self.model.get_object(my_object.id)
        self.assertEqual(MyObject, type(gotten_object_))
        self.assertEqual(my_object, gotten_object_)

    def test_del_object(self):
        my_object = MyObject()
        self.model.add_object(my_object)
        self.model.del_object(my_object.id)
        self.assertEqual(0, len(self.model.objects))
        self.assertIsNone(self.model.objects.get(my_object.id))

    def test_is_empty_objects(self):
        self.assertTrue(self.model.is_empty_objects())
        self.model.create_object(MyObject)
        self.assertFalse(self.model.is_empty_objects())

    def test_is_one_object_in_objects(self):
        self.assertFalse(self.model.is_one_object_in_objects())
        self.model.create_object(MyObject)
        self.assertTrue(self.model.is_one_object_in_objects())
        self.model.create_object(MyObject)
        self.assertFalse(self.model.is_one_object_in_objects())


if __name__ == '__main__':
    unittest.main()
