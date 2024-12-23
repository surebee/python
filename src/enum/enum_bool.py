import enum
class Num(enum.Enum):
    ZERO = 0
    ONE = 1

    def __bool__(self):
        return bool(self.value)

if __name__ == '__main__':
    print(bool(Num(0)))
    print(bool(Num['ZERO']))
    print(bool(Num(1)))
    print(bool(Num['ONE']))
