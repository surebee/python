from enum import Enum
from functools import total_ordering

@total_ordering
class EnumCompare(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2

    def __eq__(self, other):
        if isinstance(other, EnumCompare):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        return False

    def __lt__(self, other):
        if isinstance(other, EnumCompare):
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other
        return False

