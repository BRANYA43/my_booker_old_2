import config.config as cfg
from views.constructor import Constructor


class FormDialog(Constructor):
    def __init__(self, parent, size=cfg.SIZE_DIALOG):
        super().__init__(window=2, parent=parent, size=size)
        self.build_view()
