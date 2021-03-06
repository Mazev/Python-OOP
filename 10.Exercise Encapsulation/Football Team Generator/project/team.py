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
        self.__name = value

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return

        return f"Player {player_name} not found"


# p = Player("Pall", 3, 3, 3, 3, 3)
# t = Team("Best", 10)
# s = Player("Pall", 3, 3, 3, 3, 3)
# d = Player("stef", 3, 4, 3, 3, 3)
# print(Team.remove_player('beast', 'pall'))

import unittest

from project.player import Player



class Tests(unittest.TestCase):
    def test_player_init(self):
        p = Player("Pall", 3, 3, 3, 3, 3)
        self.assertEqual(p.name, "Pall")
        self.assertEqual(p.endurance, 3)
        self.assertEqual(p.sprint, 3)
        self.assertEqual(p.passing, 3)
        self.assertEqual(p.dribble, 3)
        self.assertEqual(p.shooting, 3)

    def test_player_str(self):
        p = Player("Pall", 3, 3, 3, 3, 3)
        result = str(p)
        expected = "Player: Pall\nEndurance: 3\nSprint: 3\nDribble: 3\nPassing: 3\nShooting: 3\n"
        self.assertEqual(expected, result)

    def test_team_init(self):
        t = Team("Best", 10)
        self.assertEqual(t.name, "Best")
        self.assertEqual(t.rating, 10)
        self.assertEqual(len(t.players), 0)

    def test_team_add_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)

        self.assertEqual(t.add_player(p), "Player Pall joined team Best")

    def test_team_add_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)

        t.add_player(p)
        self.assertEqual(t.add_player(p), "Player Pall has already joined")

    def test_team_remove_successful(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)
        t.add_player(p)
        exp = t.remove_player("Pall")
        self.assertEqual(exp, p)

    def test_team_remove_fail(self):
        t = Team("Best", 10)
        p = Player("Pall", 3, 3, 3, 3, 3)
        result = "Player Pall not found"
        exp = t.remove_player("Pall")
        self.assertEqual(exp, result)


if __name__ == "__main__":
    unittest.main()


player_1