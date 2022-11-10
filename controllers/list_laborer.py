import wx

from models.list import MList
from views.laborer.info import VInfo
from views.laborer.profile import VProfile
from views.laborer.list import VList
from objects.laborer import Laborer
from funcs_support import is_selected_object


class CLaborerList:
    def __init__(self, model: MList, list_view: VList):
        self.model = model
        self.list_view = list_view
        self.info_view = VInfo(self.list_view)
        self.profile_view = VProfile(self.list_view)
        self.list_view.disable_widget('info', 'edit', 'delete', widget='btn')
        self.add_binds()

    def add_binds(self):
        self.list_view.bind_btn('info', self.on_info)
        self.list_view.bind_btn('add', self.on_add)
        self.list_view.bind_btn('edit', self.on_edit)
        self.list_view.bind_btn('delete', self.on_delete)
        self.profile_view.bind_btn('save', self.on_save)
        self.info_view.bind_btn('ok', self.on_ok)
        self.list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select)

    def on_select(self, event):
        self.model.selected_row = self.list_view.list_ctrl.GetFocusedItem()
        self.model.selected_object_id = int(self.list_view.list_ctrl.GetItem(self.model.selected_row, col=1).GetText())
        self.model.selected_object = self.model.get_object(self.model.selected_object_id)

    def on_save(self, event):
        if self.model.mode_edited:
            laborer = self.model.selected_object
            self.model.set_attrs_object(laborer,
                                        name=self.profile_view.get_value_entry_field('full_name'),
                                        payment=self.profile_view.get_value_combobox('payment'),
                                        rate=self.profile_view.get_value_entry_field('rate'))
            self.list_view.set_row(self.model.selected_row, [laborer.name])
        else:
            laborer = self.model.create_object(Laborer,
                                               name=self.profile_view.get_value_entry_field('full_name'),
                                               payment=self.profile_view.get_value_combobox('payment'),
                                               rate=self.profile_view.get_value_entry_field('rate'))
            self.model.add_object(laborer)
            self.list_view.add_row(laborer.name, laborer.id)
        self.profile_view.Close()

    @is_selected_object
    def on_info(self, event):
        laborer = self.model.selected_object
        self.info_view.set_info(laborer.name, laborer.payment, str(laborer.rate))
        self.info_view.Center()
        self.info_view.ShowModal()

    def on_add(self, event):
        self.model.mode_edited = False
        self.profile_view.Center()
        self.profile_view.ShowModal()
        if self.model.is_one_object_in_objects():
            self.list_view.enable_widget('info', 'edit', 'delete', widget='btn')

    @is_selected_object
    def on_edit(self, event):
        self.model.mode_edited = True
        laborer = self.model.selected_object
        self.profile_view.set_value_entry_field('full_name', laborer.name)
        self.profile_view.set_value_combobox('payment', laborer.payment)
        self.profile_view.set_value_entry_field('rate', str(laborer.rate))
        self.profile_view.Center()
        self.profile_view.ShowModal()

    @is_selected_object
    def on_delete(self, event):
        self.model.del_object(self.model.selected_object_id)
        self.list_view.del_row(self.model.selected_row)
        self.model.set_value_selected_attrs_to_none()
        if self.model.is_empty_objects():
            self.list_view.disable_widget('info', 'edit', 'delete', widget='btn')

    def on_ok(self, event):
        self.info_view.Close()
