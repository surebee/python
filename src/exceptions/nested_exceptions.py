import json

json_str = """
    {
        "Alex": { "age": 12 },
        "Mary": { "age": 21, "city": "New York" },
        "Fred": { "age": "unknown" }
    }
"""
json_data = json.loads(json_str)
print(json_data)

class Person:
    __slots__ = "name", "_age"

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError(f"Cannot set age={value} for {self.name}")

    def __repr__(self):
        return f"{self.name} {self.age}"

persons = []
for name, attribs in json_data.items():
    p = Person(name)
    try:
        for key, value in attribs.items():
            try:
                setattr(p, key, value)
            except AttributeError:
                print(f"Ignoring unallowed attribute {name}.{key}={value}")
    except ValueError as ex:
        print(ex)
    else:
        persons.append(p)

for p in persons:
    print(p)

