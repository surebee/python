from enum import Enum, unique

class GenericException(Exception):
    pass

class Timeout(Exception):
    pass

@unique
class AppException(Enum):
    Generic = 100, GenericException, "Generic exception messgae"
    Timeout = 101, Timeout, "Timeout Exception message"
    NotAnInteger = 102, ValueError, "Value Error Exception message"


    def __new__(cls, ex_code, ex_class, ex_message):
        member = object.__new__(cls)
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message

        return member

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f"{self.code} - {message}")


if __name__ == '__main__':
    print(AppException['Generic'].value)
    print(AppException.Timeout.value)
    try:
        AppException.NotAnInteger.throw("new message")
    except ValueError as ex:
        print(f"{ex}")
