from objects.my_object import MyObject


class ListModel:
    def __init__(self):
        self.objects = {}
        self.selected_row = None
        self.selected_object_id = None
        self.selected_object = None
        self.mode_edited = False

    def set_none_selected_attrs(self):
        self.selected_row = None
        self.selected_object_id = None
        self.selected_object = None

    @staticmethod
    def set_attrs_object(object_: MyObject, **attrs_and_value):
        for attr, value in attrs_and_value.items():
            object_.__setattr__(attr, value)

    def add_object(self, object_: MyObject):
        self.objects.setdefault(object_.id, object_)

    def create_object(self, class_, **attrs_and_value):
        object_: MyObject = class_()
        self.set_attrs_object(object_, **attrs_and_value)
        self.add_object(object_)

    def get_object(self, id_: int) -> MyObject:
        return self.objects[id_]

    def del_object(self, id_: int):
        del self.objects[id_]

    def is_empty_objects(self) -> bool:
        if len(self.objects) == 0:
            return True
        return False

    def is_one_object_in_objects(self) -> bool:
        if len(self.objects) == 1:
            return True
        return False


if __name__ == '__main__':
    ...
