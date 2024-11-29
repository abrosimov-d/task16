import os, time
from helper import Helper
from pathlib import Path

class FileManager():
    def __init__(self):
        self.__functions = [
            {'name': '..', 'function': self.cd, 'argc': 0},
            {'name': 'ls', 'function': self.ls, 'argc': 0},
            {'name': 'mkdir', 'function': self.mkdir, 'argc': 0},
            {'name': 'rmdir', 'function': self.rmdir, 'argc': 0},
            {'name': 'touch', 'function': self.touch, 'argc': 0},
            {'name': 'rm', 'function': self.rm, 'argc': 0},
            {'name': 'info', 'function': self.info, 'argc': 0},
            {'name': 'exit', 'function': self.ls, 'argc': 0},
        ]

    def get_functions(self):
        return self.__functions
    
    def call_function_by_name(self, name, arg):
        result = None
        for function in self.__functions:
            if function['name'] == name:
                result = function['function'](arg)
        return result

    def cwd(swld):
        return os.getcwd()

    def ls(self):
        result = []
        for elem in os.listdir(os.getcwd()):
            file = []
            file.append(elem)
            if os.path.isdir(elem):
                file_size = '<dir>'
            else:
                try:
                    file_size = os.path.getsize(elem)
                except:
                    pass
            file.append(file_size)
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(elem)
            file.append(time.ctime(mtime))
            result.append(file)
        return result
    
    def cd(self, dir):
        os.chdir(dir)

    def info(self, filename):
        result = []

        def append_data_to_result(a, b):
            row = []
            row.append(a)
            row.append(b)
            result.append(row)

        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filename)

        append_data_to_result('path', os.getcwd())
        append_data_to_result('name', filename)
        append_data_to_result('size', os.path.getsize(filename))
        append_data_to_result('mode', mode)
        append_data_to_result('access time', time.ctime(atime))
        append_data_to_result('modified time', time.ctime(mtime))
        append_data_to_result('create time', time.ctime(ctime))

        return result

    def mkdir(self, dir):
        os.mkdir(dir)

    def rmdir(self, dir):
        os.rmdir(dir)

    def rm(self, dir):
        os.remove(dir)

    def touch(self, filename):
        Path(f'{os.getcwd()}{os.path.sep}{filename}').touch()