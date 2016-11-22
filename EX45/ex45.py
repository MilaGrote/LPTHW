from sys import exit
from ex45_levels import *


class Level(object):

    def enter(self):
        exit(1)


class Engine(object):

    def __init__(self, Level_map):
        self.Level_map = Level_map

    def play(self):
        current_Level = self.Level_map.opening_Level()
        last_Level = self.Level_map.next_Level('finished')

        while current_Level != last_Level:
            next_Level_name = current_Level.enter()
            current_Level = self.Level_map.next_Level(next_Level_name)

        current_Level.enter()

class Map(object):

    Levels = {
        'river': River(),
        'left': LeftRiverBank(),
        'right': RightRiverBank(),
        'finished': Finished()
    }

    def __init__(self, start_Level):
        self.start_Level = start_Level

    def next_Level(self, Level_name):
        val = Map.Levels.get(Level_name)
        return val

    def opening_Level(self):
        return self.next_Level(self.start_Level)

def dead(why):
    print why, " "
    exit(0)

def zombie_herd():
    print """
    They eat your brains.
    Congrats, You are now a Zombie.
    (>*_*)> ^(* _ *)^ <(*_*<)
    """
    exit(0)

a_map = Map('river')
a_game = Engine(a_map)
a_game.play()
