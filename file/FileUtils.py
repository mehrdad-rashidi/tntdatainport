import os


class FileUtils:
    __path = None

    def __init__(self, dir_path):
        self.path = dir_path

    def list_file(self) -> list:
        files = []
        directories = []
        for i in os.scandir(self.path):
            if i.is_dir():
                directories.append(i.path)
            else:
                files.append(i.path)
        return files, directories

    def make_directory(self, dir_name, dir_create_location):
        self.path = os.path.join(dir_create_location, dir_name)
        try:
            os.mkdir(self.path)
            return True
        except OSError as e:
            print(f'Could not create directory {dir_name} because : {e}')
            return False

    def create_file(self, file_name, file_extension, file_create_location):
        self.path = file_create_location
        full_name = file_name + '.' + file_extension
        self.path = self.path + '/' + full_name
        try:
            open(self.path, 'a').close()

        except OSError as e:
            print(f'Could not create file {full_name} reason is : {e}')
        else:
            return self.path, full_name

    def delete_file(self, full_name, file_location):
        self.path = os.path.join(file_location, full_name)
        try:
            os.remove(self.path)
            return True
        except OSError as e:
            print(f'count not delete file {self.path} reason is : {e}')
            return False

    def remove_empty_directory(self, directory_location, dir_name):
        self.path = os.path.join(directory_location, dir_name)
        try:
            os.rmdir(self.path)
        except OSError as e:
            print(f' Could not remove directory {dir_name} because : {e}')

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, directory_path):
        self.__path = directory_path
