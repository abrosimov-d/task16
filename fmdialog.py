from dialog import Dialog
from  helper import Helper

class FileManagerDialog(Dialog):
    def __init__(self):
        super().__init__()
        template = '''
            size, XXL, 0, 0
            header, 🚀TASK16, 0, 0
            tab, FM, 0, 0
            toolbar, 0, 1000, mkdir, rmdir, touch, rm, exit
            -separator, 0, 0, 0
            treeview, 0, 999, name, size, time
            tab, AB, 1, 1
            xlabel, FILE MANAGER, 0, 0
            label, assignment for python course, 0, 0
            label, used: tkinter, 0, 0 
            label, date: XX.11.2024, 0, 0
            urlbutton, https://github.com/abrosimov-d/task16, 0, 0
'''
        data = []
        for _ in range(20):
            file = []
            file.append(Helper.random_filename())
            file.append(Helper.random_filesize())
            data.append(file)

        super().template(template)
        self.set_data_to_treeview(999, data)
        super().set_event_listener(self.__event_listener)
        super().run()

    def __event_listener(self, event, id, event_data):
        if event == 'close':
            return True