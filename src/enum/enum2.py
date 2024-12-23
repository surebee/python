import enum

class NumSides(enum.Enum):
    Triangle = 3
    Rectangle = 4
    Square = 4
    Rhombus = 4

if __name__ == '__main__':
    print(NumSides.__members__)
    assert str(NumSides(4)) == 'NumSides.Rectangle'
