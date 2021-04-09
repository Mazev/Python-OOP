class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.__budget = budget
        self.__workers_capacity = workers_capacity
        self.__animlal_capacit = animlal_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= and len(self.__animlal_capacit) < self.__animlal_capacit:
            self.animals.append(animal)
            return f"{self.name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.name) < self.__animlal_capacit and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{self.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker_name)
            return f"{worker_name} fired successfully"
        except KeyError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries_to_pay = sum([w.salary for w in self.workers])
        if self.__budget >= all_salaries_to_pay:
            self.__budget -= all_salaries_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_costs_for_animals = sum([a.get_needs() for a in self.animals])
        if self.__budget >= all_costs_for_animals:
            self.__budget -= all_costs_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        res = f"You have {len(self.animals)} animals" + "\n"
        res += f"----- {lions} Lions:"
        res += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        res += f"----- {tigers} Lions:"
        res += "{}".format('\n'.join([repr(l) for l in tigers])) + '\n'
        res += f"----- {cheetahs} Lions:\n"
        res += "{}".format('\n'.join([repr(l) for l in cheetahs])) + "\n"
        return res


    def workers_status(self):

        keepers = [ w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vet = keepers = [ w for w in self.workers if w.__class__.__name__ == "Vets"]
        res = f"You have {len(self.workers)} workers" + "\n"

        res += f"You have {len(keepers)} workers" + "\n"
        res += f"----- {keepers} Keepers:"
        res += "{}".format('\n'.join([w for w in caretakers])) +" \n"
        res += f"----- {caretakers} Keepers:"
        res += "{}".format('\n'.join([w for w in keepers])) + '\n'
        res += f"----- {vet} Keepers:"
        res += "{}".format('\n'.join([w for w in vet])) + '\n'