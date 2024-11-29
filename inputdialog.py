from dialog import Dialog
from helper import Helper

ID_INPUT_INPUT = Helper.random_id()
ID_BUTTON_YES = Helper.random_id()
ID_BUTTON_NO = Helper.random_id()

class InputDialog(Dialog):
    def __init__(self, parent, message):
        super().__init__(parent)
        template = f'''
            size, L, 0, 0
            separator, 0, 0, 0
            label, {message}, 0, 0
            input, ,{ID_INPUT_INPUT}, 0
            button, ok, {ID_BUTTON_YES}, 0, 0
            button, cancel, {ID_BUTTON_NO}, 0, 0
        '''
        super().template(template)
        super().set_event_listener(self.__event_listener)
        super().set_focus_by_id(ID_INPUT_INPUT)
        self.result = None

    def show(self):
        super().run()
        return self.result

    def __event_listener(self, event, id, event_data):
        if event == 'init':
            pass

        if event == 'click' and id == ID_BUTTON_YES:
            self.result = self.get_text_by_id(ID_INPUT_INPUT)
            super().close_window()

        if event == 'click' and id == ID_BUTTON_NO:
            super().close_window()

        if event == 'close':
            return True