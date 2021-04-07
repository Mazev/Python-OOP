class MovieWorld:


    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        return

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)



    def rent_dvd(self, customer_id, dvd_id):
        customer = [ c for c in customer_id if c.id == customer_id]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd_id in [id for id in customer.rented_dvds][0]:
            return f"{customer.name} has already rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        pass

from project.customer import Customer
from project.dvd import DVD


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
