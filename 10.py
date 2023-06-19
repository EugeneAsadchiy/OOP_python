class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(self, role):
        if role in Access.__access_list:
            return True
        else:
            return False

    @staticmethod
    def get_access(self):
        if not isinstance(self, User):
            print("AccessTypeError")
        elif Access.__check_access(self, self.role):
            print(f"User {self.name}: success")
        else:
            print("AccessDenied")
