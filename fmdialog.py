from dialog import Dialog
from helper import Helper
from yesnodialog import YesNoDialog
from inputdialog import InputDialog

ID_TREEVIEW_FILES = Helper.random_id()
ID_TOOLBAR = Helper.random_id()
ID_LABEL_ERROR = Helper.random_id()
ID_TREEVIEW_PROPERTIES = Helper.random_id()
ID_LABEL_FILENAME = Helper.random_id()
ID_LABEL_CWD = Helper.random_id()

class FileManagerDialog(Dialog):
    def __init__(self, command_listener, functions):
        super().__init__(None)
        self.__command_listener = command_listener
        self.functions = functions
        template = f'''
            size, XXL, 0, 0
            header, 🚀TASK16, 0, 0
            tab, FM, 0, 0
            toolbar, 0, {ID_TOOLBAR}, {','.join([str(function['name']) for function in functions])}
            label,,{ID_LABEL_CWD}, 0, 0 
            treeview, 0, {ID_TREEVIEW_FILES}, name, size, time
            slabel, error, {ID_LABEL_ERROR}, 0
            tab, IN, 1, 1
            label,, {ID_LABEL_FILENAME}, 0
            treeview, 0, {ID_TREEVIEW_PROPERTIES}, property, value
            tab, AB, 2, 2
            xlabel, FILE MANAGER, 0, 0
            label, assignment for python course, 0, 0
            label, used: tkinter, 0, 0 
            label, date: XX.11.2024, 0, 0
            urlbutton, https://github.com/abrosimov-d/task16, 0, 0
'''
        super().template(template)
        super().set_event_listener(self.__event_listener)
        super().run()

    def __event_listener(self, event, id, event_data):

        if event == 'close':
            return True
        
        if event == 'init':
            command = {}
            command['name'] = 'ls'
            result = self.__command_listener(command)
            self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
            self.set_text_by_id(ID_LABEL_CWD, command['cwd'])
            if 'error' in command:
                self.set_text_by_id(ID_LABEL_ERROR, command['error'])
            else:
                self.set_text_by_id(ID_LABEL_ERROR, '')

        if (event == 'key' and id == ID_TREEVIEW_FILES and event_data.char == '\r') or (event == 'click' and id == ID_TREEVIEW_FILES):
            item = self.get_item_selected(ID_TREEVIEW_FILES)
            if item == None:
                return
            if item[1] != '<dir>':
                command = {}
                command['name'] = 'info'
                command['arg'] = item[0]
                self.__command_listener(command)
                self.set_text_by_id(ID_LABEL_FILENAME, command['arg'])
                self.set_data_to_treeview(ID_TREEVIEW_PROPERTIES, command['result'])
                self.set_active_tab(1)
            else:
                command = {}
                command['name'] = 'cd'
                command['arg'] = item[0]
                result = self.__command_listener(command)
                self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
                self.set_text_by_id(ID_LABEL_CWD, command['cwd'])
                if 'error' in command:
                    self.set_text_by_id(ID_LABEL_ERROR, command['error'])
                else:
                    self.set_text_by_id(ID_LABEL_ERROR, '')

        if event == 'click' and id == ID_TOOLBAR and event_data == 0:
            command = {}
            command['name'] = 'cd'
            command['arg'] = '..'
            result = self.__command_listener(command)
            self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
            self.set_text_by_id(ID_LABEL_CWD, command['cwd'])
            if 'error' in command:
                self.set_text_by_id(ID_LABEL_ERROR, command['error'])
            else:
                self.set_text_by_id(ID_LABEL_ERROR, '')

        elif event == 'click' and id == ID_TOOLBAR:
            command_name = self.functions[event_data]['name']
            match command_name:
                case 'info':
                    item = self.get_item_selected(ID_TREEVIEW_FILES)
                    if item == None:
                        return
                    command = {}
                    command['name'] = self.functions[event_data]['name']
                    command['arg'] = item[0]
                    self.__command_listener(command)
                    self.set_text_by_id(ID_LABEL_FILENAME, command['arg'])
                    self.set_data_to_treeview(ID_TREEVIEW_PROPERTIES, command['result'])
                    self.set_active_tab(1)

                case 'mkdir' | 'touch':
                    input_dialog = InputDialog(self, f'input argument for {command_name}')
                    result = input_dialog.show()
                    if result != None:
                        command = {}
                        command['name'] = command_name
                        command['arg'] = result
                        self.__command_listener(command)
                        self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
                        if 'error' in command:
                            self.set_text_by_id(ID_LABEL_ERROR, command['error'])
                        else:
                            self.set_text_by_id(ID_LABEL_ERROR, '')

                case 'ls':
                    command = {}
                    command['name'] = command_name
                    self.__command_listener(command)
                    self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
                    self.set_text_by_id(ID_LABEL_CWD, command['cwd'])
                    if 'error' in command:
                        self.set_text_by_id(ID_LABEL_ERROR, command['error'])
                    else:
                        self.set_text_by_id(ID_LABEL_ERROR, '')

                case 'rmdir'|'rm':
                    item = self.get_item_selected(ID_TREEVIEW_FILES)
                    if item == None:
                        return
                    yesno = YesNoDialog(self, '', f'a you sure {command_name} {item[0]}?')
                    if yesno.show():
                        command = {}
                        command['name'] = command_name
                        command['arg'] = item[0]
                        self.__command_listener(command)
                        self.set_data_to_treeview(ID_TREEVIEW_FILES, command['result'])
                        if 'error' in command:
                            self.set_text_by_id(ID_LABEL_ERROR, command['error'])
                        else:
                            self.set_text_by_id(ID_LABEL_ERROR, '')

                case 'exit':
                    yesno = YesNoDialog(self, '', f'do you want {command_name}?')
                    if yesno.show():
                        super().close_window()





        
            
