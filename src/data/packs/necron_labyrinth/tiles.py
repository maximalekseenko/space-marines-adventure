from data import Tile


class Tile_Wall(Tile):
    KEY = "NLTW"
    VARIABLES = {
        'wall':True,
    }

class Tile_Passage(Tile):
    KEY = "NLTP"
    VARIABLES = {}


class Tile_Console(Tile):
    KEY = "NLTC"
    VARIABLES = {
        'active':False,
    }