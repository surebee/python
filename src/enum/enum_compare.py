import enum
class Num(enum.Enum):
    ZERO = 0
    ONE = 1
    TWO = 2

    def __lt__(self, other):
        return isinstance(other, Num) and self.value < other.value

if __name__ == '__main__':
    print(Num(0) <  Num(1))
    print(Num(2) >  Num(1))
    print(Num(0) >  Num(2))
