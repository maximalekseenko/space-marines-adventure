from data import Tile


class Tile_Wall(Tile):
    KEY = "NLTWall"
    ATTRS = {
        'wall':True,
    }

class Tile_Passage(Tile):
    KEY = "NLTPassage"
    ATTRS = {}


class Tile_Console(Tile):
    KEY = "NLTConsole"
    ATTRS = {
        'console':True,
        'active':False,
    }

class Tile_Portal(Tile):
    KEY = "NLTPortal"
    ATTRS = {
        'portal':True,
    }