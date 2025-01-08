
class ConversionError(Exception):
    pass

def convert_str(value):
    if not isinstance(value, str):
        raise TypeError()

    value = value.casefold()

    if value not in {'t', 'f', 'true', 'false', '1', '0'}:
        raise ValueError(f"{value=} should be 't', 'f', 'true', 'false', '1', '0'")

    return bool(value)

def convert_int(value):
    if not isinstance(value, int):
        raise TypeError()

    if value not in {0, 1}:
        raise ValueError(f"{value=} should be 0 or 1")

    return bool(value)


def make_bool(value):
    try:
        try:
            v = convert_int(value)
        except TypeError:
            try:
                v = convert_str(value)
            except TypeError as ex:
                raise ConversionError(f"Invalid type to convert {ex}")
    except ValueError as ex:
        raise ConversionError(f"Invalid value to convert {ex}")
    else:
        return v

for elem in [1, 2, "true", "false", True, False, 'A', ["some"]]:
    try:
        result = make_bool(elem)
    except ConversionError as ex:
       result = str(ex)

    print(f"{elem} = {result}")

