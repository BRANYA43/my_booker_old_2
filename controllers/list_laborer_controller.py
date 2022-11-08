import wx

from models.list_ctrl_model import ListCtrlModel
from views.info_laborer import InfoLaborer
from views.profile_laborer import ProfileLaborer
from views.list_laborer import ListLaborer
from objects.laborer import Laborer
from funcs_support import is_selected_object


class ListLaborerController:
    def __init__(self, model: ListCtrlModel, info_view: InfoLaborer, profile_view: ProfileLaborer, list_view: ListLaborer):
        self.model = model
        self.info_view = info_view
        self.profile_view = profile_view
        self.list_view = list_view

    def add_binds(self):
        self.list_view.bind_btn('info', self.on_info)
        self.list_view.bind_btn('add', self.on_add)
        self.list_view.bind_btn('edit', self.on_edit)
        self.list_view.bind_btn('delete', self.on_delete)
        self.profile_view.bind_btn('save', self.on_save)
        self.info_view.bind_btn('ok', self.on_ok)
        self.profile_view.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.on_select, self.list_view.list_ctrl)

    def on_select(self, event):
        self.model.selected_row = self.list_view.list_ctrl.GetFocusedItem()
        self.model.selected_object_id = int(self.list_view.list_ctrl.GetItem(row, col=1).GetText())
        self.model.selected_object = self.model.get_object(self.model.selected_object_id)

    def on_save(self, event):
        if self.model.mode_edited:
            laborer = self.model.selected_object
            self.model.set_attrs_object(Laborer,
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
        self.profile_view.Destroy()

    @is_selected_object
    def on_info(self, event):
        self.info_view.ShowModal()
        laborer = self.model.selected_object
        self.info_view.set_info(laborer.name, laborer.payment, str(laborer.rate))

    def on_add(self, event):
        self.model.mode_edited = False
        self.profile_view.ShowModal()

    @is_selected_object
    def on_edit(self, event):
        self.model.mode_edited = True
        self.profile_view.ShowModal()
        laborer = self.model.selected_object
        self.profile_view.set_value_entry_field('full_name', laborer.name)
        self.profile_view.set_value_combobox('payment', laborer.payment)
        self.profile_view.set_value_entry_field('rate', str(laborer.rate))

    @is_selected_object
    def on_delete(self, event):
        self.model.del_object(self.model.selected_object_id)
        self.list_view.del_row(self.model.selected_row)
        self.model.set_value_selected_attrs_to_none()

    def on_ok(self, event):
        self.info_view.Destroy()
