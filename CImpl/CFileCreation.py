class CFileCreation:
    def __init__(self):
        self.files = {}

    def add_file(self, file_name : str, code : str):
        if file_name in self.get_file_names():
            raise Exception("File '{}' already exists, use update_file() instead".format(file_name))
        self.files[file_name] = code
    
    def update_file(self, file_name : str, code : str):
        if not (file_name in self.files):
            raise Exception("File '{}' does not exist, use add_file() instead".format(file_name))
        self.files[file_name] = code

    def get_code(self, file_name : str) -> str:
        if not (file_name in self.files):
            raise Exception("Cannot get code from '{}' : file does not exist".format(file_name))
        return self.files[file_name]

    def get_files(self) -> dict:
        return self.files

    def get_file_names(self) -> list:
        return self.files.keys()

    def create_empty_c_file(self,filename):
        self.add_file(filename, "")

    def create_main_file(self):
        self.create_empty_c_file("main.c")
        code_main = """
        int main() {
            // TODO
            return 0;
        }
        """
        self.update_file("main.c", code_main)
