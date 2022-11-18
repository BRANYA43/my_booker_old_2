from builders.frame import FrameBuilder


class TestFrame(FrameBuilder):
    def __init__(self, window, *attr):
        super().__init__(parent=None, title='TEST-FRAME', size=(800, 600))
        self.window = window(self, *attr)

    def create_widgets(self):
        pass

    def build_view(self):
        pass

    def show_frame(self):
        self.Center()
        self.Show()

    def show_dialog(self):
        self.window.Center()
        self.window.ShowModal()


if __name__ == '__main__':
    ...
