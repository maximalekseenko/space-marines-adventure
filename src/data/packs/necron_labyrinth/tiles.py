from data import Tile


class Tile_Wall(Tile):
    KEY = "NLTWall"
    VARIABLES = {
        'wall':True,
    }

class Tile_Passage(Tile):
    KEY = "NLTPassage"
    VARIABLES = {}


class Tile_Console(Tile):
    KEY = "NLTConsole"
    VARIABLES = {
        'console':True,
        'active':False,
    }

class Tile_Portal(Tile):
    KEY = "NLTPortal"
    VARIABLES = {
        'portal':True,
    }