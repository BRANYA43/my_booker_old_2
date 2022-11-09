from objects.my_object import MyObject


class MList:
    def __init__(self):
        self.objects = {}
        self.selected_row = None
        self.selected_object_id = None
        self.selected_object = None
        self.mode_edited = False

    def add_object(self, object_: MyObject):
        self.objects.setdefault(object_.id, object_)

    def del_object(self, id_: int):
        del self.objects[id_]

    def get_object(self, id_: int) -> MyObject:
        return self.objects[id_]

    def create_object(self, class_, **attrs_and_value) -> MyObject:
        object_: MyObject = class_()
        self.set_attrs_object(object_, **attrs_and_value)
        return object_

    @staticmethod
    def set_attrs_object(object_, **attrs_and_value):
        for attr, value in attrs_and_value.items():
            object_.__setattr__(attr, value)
        return object_

    def set_value_selected_attrs_to_none(self):
        self.selected_row = None
        self.selected_object_id = None
        self.selected_object = None


if __name__ == '__main__':
    list_model = MList()

    object_ = list_model.create_object(MyObject, name='Triangle')
    list_model.add_object(object_)
    print(list_model.objects)
    print(list_model.get_object(object_.id))
    list_model.del_object(object_.id)
    print(list_model.objects)
