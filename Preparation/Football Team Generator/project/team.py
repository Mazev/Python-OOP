from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        try:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"


player_1 = Player("A1", 6, 6, 6,6,6)
player_2 = Player("A2", 2, 1, 6,6,6)

t = Team("stefan", 10)

print(t.add_player(player_1))
print(t.add_player(player_1))


print(t.remove_player("A1"))
print(t.remove_player("A1"))
import unittest

#
# from project.player import Player
# from project.team import Team
#
#
# class Tests(unittest.TestCase):
#     def test_player_init(self):
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         self.assertEqual(p.name, "Pall")
#         self.assertEqual(p.endurance, 3)
#         self.assertEqual(p.sprint, 3)
#         self.assertEqual(p.passing, 3)
#         self.assertEqual(p.dribble, 3)
#         self.assertEqual(p.shooting, 3)
#
#     def test_player_str(self):
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         result = str(p)
#         expected = "Player: Pall\nEndurance: 3\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3\n"
#         self.assertEqual(expected, result)
#
#     def test_team_init(self):
#         t = Team("Best", 10)
#         self.assertEqual(t.name, "Best")
#         self.assertEqual(t.rating, 10)
#         self.assertEqual(len(t.players), 0)
#
#     def test_team_add_successful(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#
#         self.assertEqual(t.add_player(p), "Player Pall joined team Best")
#
#     def test_team_add_fail(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#
#         t.add_player(p)
#         self.assertEqual(t.add_player(p), "Player Pall has already joined")
#
#     def test_team_remove_successful(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         t.add_player(p)
#         exp = t.remove_player("Pall")
#         self.assertEqual(exp, p)
#
#     def test_team_remove_fail(self):
#         t = Team("Best", 10)
#         p = Player("Pall", 3, 3, 3, 3, 3)
#         result = "Player Pall not found"
#         exp = t.remove_player("Pall")
#         self.assertEqual(exp, result)
#
#
# if __name__ == "__main__":
#     unittest.main()
