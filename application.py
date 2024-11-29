from fmdialog import FileManagerDialog
from filemanager import FileManager
from time import sleep

class Application():
    def __init__(self):
        self.file_manager = FileManager()
        self.fmdialog = FileManagerDialog(self.command_listener, self.file_manager.get_functions())

    def command_listener(self, command):
        match command['name']:
            case 'ls':
                try:
                    command['result'] = self.file_manager.ls()
                except Exception as e:
                    command['error'] = e

            case 'cd':
                try:
                    self.file_manager.cd(command['arg'])
                except Exception as e:
                    command['error'] = e
                command['result'] = self.file_manager.ls()

            case _:
                try:
                    command['result'] = self.file_manager.call_function_by_name(command['name'], command['arg'])
                except Exception as e:
                    command['error'] = e
                if command['name'] != 'info':
                    command['result'] = self.file_manager.ls()
        
        command['cwd'] = self.file_manager.cwd()
        return command
    
    def sleep(self):
        sleep(3)