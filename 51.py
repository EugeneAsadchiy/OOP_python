class PasswordInvalidError(Exception):
    pass


class PasswordLengthError(PasswordInvalidError):
    pass


class PasswordContainUpperError(PasswordInvalidError):
    pass


class PasswordContainDigitError(PasswordInvalidError):
    pass


class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, password):
        if len(password) < 8:
            raise PasswordLengthError("Пароль должен быть не менее 8 символов")
        elif not any(map(str.isupper, password)):
            raise PasswordContainUpperError("Пароль должен содержать хотя бы одну заглавную букву")
        elif not any(map(str.isdigit, password)):
            raise PasswordContainDigitError("Пароль должен содержать хотя бы одну цифру")
        else:
            self.password = password


# Ниже код для проверки

assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'
