from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    # from .campaign import Campaign
    # from .map import Map
    # from .entity import Entity
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

        # create parameters
        self.campaign = __campaign
        '''Current campaign. \n\n Do not edit directly! Use corresponding functions!'''

        self.variables:dict[str, any] = dict()
        '''Current variables. \n\n Do not edit directly! Use corresponding functions!'''

        # entity
        self.entities:list[any] = list()
        '''Current entities. \n\n Do not edit directly! Use corresponding functions!'''

        self.entity_free_id:int = 0
        '''Free id to give to newly created entity.'''

        # tile
        self.tiles:list[Tile] = list()
        '''Current tiles. \n\n Do not edit directly! Use corresponding functions!'''

        self.tiles_free_id:int = 0
        '''Free id to give to newly created tile.'''

        self.tile_grid:list[list[list[Tile]]] = [[list() for _ in range(self.MAP_SIZE[1])] for _ in range(self.MAP_SIZE[0])]  
        '''Tiles sorted by position and layer.'''

        # add defaults
        ## variables
        for __key, __value in self.VARIABLES.items():
            self.Variable_Create(__key, __value)

        ## entities
        # TODO

        ## tiles
        for __key, __variables in self.TILES:
            self.Tile_Create(__key, __variables)



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
    def Entity_Add(self, __entity_type:type[Entity]) -> None:

        # create new entity and give it a new id
        __new_entity = __entity_type(self.entity_free_id)
        self.entity_free_id += 1

        # add new entity to the list
        self.entities.append(__new_entity)


    def Entity_Rem(self, __entity_id:int) -> None:
        
        # find entity by id
        __todel_entity = self.Entity_Get(__entity_id)

        # delete
        self.entities.remove(__todel_entity)


    def Entity_Get(self, __entity_id:int) -> Entity:
        for __entity in self.entities:
            if __entity.id == __entity_id:
                return __entity

        # not found
        return None


    # ----- Tiles functions -----
    def Tile_Create(self, __key:str, __variables:dict[str, any] = dict()):

        # create new entity and give it a new id
        __new_tile = self.DATABASE.Get_Tile(__key)(self.tiles_free_id)
        self.tiles_free_id += 1

        # set variables
        for __key, __value in __variables.items():
            __new_tile.Variables_Set(__key, __value)

        # add new entity to the lists
        ## global
        self.tiles.append(__new_tile)
        ## positional
        self.tile_grid[__new_tile.variables['x']][__new_tile.variables['y']].append(__new_tile)



    def Tile_Rem(self, __tile:type[Tile]):
        pass



    def Get_Data(self):
        return {
            'key': self.KEY,
            'var': self.VARIABLES,
            'ent': self.ENTITIES,
            'map': self.MAP.Get_Data()
        }


    def Handle_Hero_Request(self, request:dict):
        if self.stage == "preparation":
            self.Handle_Hero_Preparation(request)


    def _Handle_Hero_Preparation(self, request:dict):
        if request['type'] == "select":
            pass



    
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