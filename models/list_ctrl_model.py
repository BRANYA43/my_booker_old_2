from objects.my_object import MyObject


class ListCtrlModel:
    def __init__(self):
        self.objects = {}

    def add_object(self, object_: MyObject):
        self.objects.setdefault(object_.id, object_)

    def del_object(self, id_: int):
        del self.objects[id_]

    def get_object(self, id_: int) -> MyObject:
        return self.objects[id_]

    @staticmethod
    def create_object(class_, **attrs_and_value) -> MyObject:
        object_: MyObject = class_()
        for attr, value in attrs_and_value.items():
            object_.__setattr__(attr, value)
        return object_


if __name__ == '__main__':
    list_model = ListCtrlModel()

    object_ = list_model.create_object(MyObject, name='Triangle')
    list_model.add_object(object_)
    print(list_model.objects)
    print(list_model.get_object(object_.id))
    list_model.del_object(object_.id)
    print(list_model.objects)
