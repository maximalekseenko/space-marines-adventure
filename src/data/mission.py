from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    # from .campaign import Campaign
    # from .map import Map
    from .entity import Entity
    from .tile import Tile
    from .database import DataBase



class Mission:

    DATABASE:DataBase
    '''Instance of database this mission is imported to.'''

    KEY:str = ""

    MAP_SIZE:tuple[int, int] = (0, 0)

    VARIABLES:dict[str, any] = dict()
    '''Default variables. \n\n Export/Import parameter.'''
    ENTITIES:list[tuple[str, dict[str, any]]] = list()
    '''Default entities. \n\n Stored as [`<entity key>`, {`<variable key>`, `<variable value>`}] \n\n Export/Import parameter.'''
    TILES:list[tuple[str, dict[str, any]]] = list()
    '''Default tiles. \n\n Stored as [`<tile key>`, {`<variable key>`, `<variable value>`}] \n\n Export/Import parameter.'''


    def __init__(self, __campaign:any) -> None:

        # create current
        ## campaign
        self.campaign = __campaign
        '''Current campaign.'''

        ## variables
        self.variables:dict[str, any] = dict()
        '''Current variables.'''

        ## entity
        self.entities:list[Entity] = list()
        '''Current entities.'''

        self.entity_free_id:int = 0
        '''Free id to give to newly created entity.'''

        self.entity_grid:list[list[Tile]] = [[None for _ in range(self.MAP_SIZE[1])] for _ in range(self.MAP_SIZE[0])]  
        '''Entities by position.'''

        ## tile
        self.tiles:list[Tile] = list()
        '''Current tiles. \n\n Do not edit directly! Use corresponding functions!'''

        self.tiles_free_id:int = 0
        '''Free id to give to newly created tile.'''

        self.tile_grid:list[list[Tile]] = [[None for _ in range(self.MAP_SIZE[1])] for _ in range(self.MAP_SIZE[0])]  
        '''Tiles by position.'''

        # add defaults
        ## variables
        for __key, __value in self.VARIABLES.items():
            self.Variable_Create(__key, __value)

        ## entities
        for __key, __variables in self.ENTITIES:
            self.Entity_Create(__key, __variables)

        ## tiles
        for __key, __variables in self.TILES:
            self.Tile_Create(__key, __variables)


    def __abs_repr__(self) -> str:
        __ret_str =  f"Mission(abstract):"
        __ret_str += f"\n├key: {self.KEY}"

        # variables
        __ret_str += f"\n├variables:"
        for __key, __value in self.VARIABLES: __ret_str += f"\n│├{__key}: {__value}"

        # entities
        # __ret_str += f"\n├entities: {self.ENTITIES}"
        # TODO list

        # tiles
        __ret_str += f"\n├tiles:"
        for __key, __variables in self.TILES: 
            __ret_str += f"\n│├key: {__key}"
            for __key, __value in __variables.items():
                __ret_str += f"\n││├{__key}: {__value }"

        # return
        return __ret_str


    def __repr__(self) -> str:
        __ret_str =  f"Mission:"
        __ret_str += f"\n├key: {self.KEY}"

        # variables
        __ret_str += f"\n├variables:"
        for __key, __value in self.variables: __ret_str += f"\n│├{__key}: {__value}"

        # entities
        __ret_str += f"\n├entities: {self.entities}"
        # TODO list

        # tiles
        __ret_str += f"\n├tiles:"
        for __tile in self.tiles: __ret_str += "\n│├" + repr(__tile).replace('\n', "\n││")

        # return
        return __ret_str


    # ----- Campaign functions -----
    # ----- Variable functions -----
    def Variable_Set(self, __key:str, __value:any) -> None:
        self.variables[__key] = __value


    def Variable_Create(self, __key:str, __value:any=None) -> None:
        self.variables[__key] = __value


    def Variable_Exists(self, __key:str) -> bool:
        return __key in self.variables


    def Variable_Get(self, __key:str) -> any:
        return self.variables[__key]


    # ----- Entities functions -----
    def Entity_Create(self, __key:str, __variables:dict[str, any] = dict()):

        # create new entity and give it a new id
        __new_entity = self.DATABASE.Get_Entity(__key)(self.entity_free_id)
        self.entity_free_id += 1

        # set variables
        for __key, __value in __variables.items():
            __new_entity.Variables_Set(__key, __value)

        # add new entity to the lists
        ## global
        self.entities.append(__new_entity)
        ## positional
        self.entity_grid[__new_entity.Variables_Get('x')][__new_entity.Variables_Get('y')] = __new_entity


    def Entity_Remove(self, __key:str):
        pass


    def Entity_Get_By_Position(self, __x, __y) -> Entity:
        return self.entity_grid[__x][__y]


    def Entity_Get_By_Id(self, __id) -> Entity:
        for __entity in self.entities:
            if __entity.id == __id:
                return __entity
        return None



    # ----- Tiles functions -----
    def Tile_Create(self, __key:str, __variables:dict[str, any] = dict()):

        # create new tile and give it a new id
        __new_tile = self.DATABASE.Get_Tile(__key)(self.tiles_free_id)
        self.tiles_free_id += 1

        # set variables
        for __key, __value in __variables.items():
            __new_tile.Variables_Set(__key, __value)

        # add new tile to the lists
        ## global
        self.tiles.append(__new_tile)
        ## positional
        self.tile_grid[__new_tile.Variables_Get('x')][__new_tile.Variables_Get('y')] = __new_tile


    def Tile_Remove(self, __tile:type[Tile]):
        pass


    def Tile_Get_By_Position(self, __x, __y) -> Tile:
        return self.tile_grid[__x][__y]


    def Tile_Get_By_Id(self, __id) -> Tile:
        for __tile in self.tiles:
            if __tile.id == __id:
                return __tile
        return None
