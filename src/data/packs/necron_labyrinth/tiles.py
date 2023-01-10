from data import Tile


class Tile_Wall(Tile):
    KEY = "NLTWall"
    DEFAULT_ATTRS = {
        'wall':True,
    }

class Tile_Passage(Tile):
    KEY = "NLTPassage"
    DEFAULT_ATTRS = {}


class Tile_Console(Tile):
    KEY = "NLTConsole"
    DEFAULT_ATTRS = {
        'console':True,
        'active':False,
    }

class Tile_Portal(Tile):
    KEY = "NLTPortal"
    DEFAULT_ATTRS = {
        'portal':True,
    }