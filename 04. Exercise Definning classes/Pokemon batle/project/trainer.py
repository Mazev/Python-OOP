from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if name not in self.pokemon:
            self.pokemon.append(name)
            return f"Caught {pokemon_details()} with health {pokemon_health}"

        if self.name in self.pokemon:
            return f"This pokemon is already caught"
        return


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
