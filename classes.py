from main import datefmt

class Student:
    University = 'MIT'
    def _init_(self, name, date_string, %args):
        self.name = name
        self.birthdate = datefmt(date_string)
