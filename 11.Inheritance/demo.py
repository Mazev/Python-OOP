class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def __repr__(self):
        return f"{self.name}: {self.age}"

    def get_object_by_attr_value(objects, **kwargs):
        result = []
        for obj in objects:
            is_valid = True
            for key, value in kwargs.items():
                if getattr(obj, key, None) != value:
                    is_valid = False
                    break

            if is_valid:
            result.append(obj)
        return result

people = [
    Person("Pesho", 12),
    Person("Gosho", 10)
]
print(get_object_by_attr_value(people, age = 12))


