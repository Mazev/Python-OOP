class Person:
    last_id = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.last_id += 1
        self.id = Person.last_id

    def say_hello(self):
        print(f"Hello , I am {self.name} and I have id {self.id}")


pesho = Person('Pesho', 11)
print(Person.last_id)
people = [pesho, Person('Gosho', 3)]
[p.say_hello() for p in people]