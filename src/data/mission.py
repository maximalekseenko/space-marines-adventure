from __future__ import annotations
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING: 
    from .entity import Entity
    from .tile import Tile
    from .database import DataBase



class Mission:

    DATABASE:DataBase
    '''Instance of database this mission is imported to.'''

    KEY:str = ""

    MAP_SIZE:tuple[int, int] = (0, 0)

    DEFAULT_ATTRS:dict[str, Any] = dict()
    '''Default attributes and their values, that applied upon creation.'''
    DEFAULT_ENTITIES:list[tuple[str, dict[str, Any]]] = list()
    '''Default entities and teir attributes, that added upon creation. \n\n Stored as [`<entity key>`, {`<variable key>`, `<variable value>`}]'''
    DEFAULT_TILES:list[tuple[str, dict[str, Any]]] = list()
    '''Default tiles and teir attributes, that added upon creation. \n\n Stored as [`<tile key>`, {`<variable key>`, `<variable value>`}]'''


    def __init__(self, __campaign:Any) -> None:

        # create current
        ## campaign
        self.campaign = __campaign
        '''Current campaign.'''

        ## attributes
        self.attrs:dict[str, Any] = dict()
        '''Current variables.'''

        ## entity
        self.entities:list[Entity] = list()
        '''Current entities.'''

        self.entity_free_id:int = 0
        '''Free id to give to newly created entity.'''

        ## tile
        self.tiles:list[Tile] = list()
        '''Current tiles.'''

        self.tiles_free_id:int = 0
        '''Free id to give to newly created tile.'''

        # add defaults
        ## variables
        self.Set_Attrs(self.DEFAULT_ATTRS)

        ## entities
        for __key, __attrs in self.DEFAULT_ENTITIES:
            self.Create_Entity(__key, __attrs)

        ## tiles
        for __key, __attrs in self.DEFAULT_TILES:
            self.Tile_Create(__key, __attrs)


    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.attrs} {self.entities} {self.tiles}>"


    def __str__(self) -> str:
        return f"<{self.__class__.__name__}>"


    # Attributes
    def Set_Attr(self, __key:str, __value:Any) -> None:
        """Sets value to attribute by key."""

        self.attrs[__key] = __value


    def Set_Attrs(self, __attrs:dict[str, Any]) -> None:
        """Sets values to attributes by key."""

        for __key, __value in __attrs.items():
            self.Set_Attr(__key, __value)


    def Get_Attr(self, __key:str) -> Any|None:
        """Get attribute value by key.
        \n If not found return None
        """

        return self.attrs.get(__key, None)


    def Exists_Attr(self, __key:str) -> bool:
        """Checks if attribute exists by key."""

        return __key in self.attrs


    def Exists_Attrs(self, __keys:list[str]) -> bool:
        """Checks if attributes exists by keys."""

        return all(__key in self.attrs for __key in __keys)


    def Check_Attr(self, __key:str, __value:Any) -> bool:
        """Checks if attribute has given value by key."""

        return self.Get_Attr(__key) == __value


    def Check_Attrs(self, __attrs:dict[str, Any]) -> bool:
        """Checks if attributes has given values by keys."""

        return all(self.Check_Attr(__key, __value) for __key, __value in __attrs.items())


    # ----- Entities functions -----
    # entity
    def Create_Entity(self, __key:str, __attrs:dict[str, Any] = dict()) -> None:
        """Creates an entity with given attrs added to default."""

        # create new entity and give it a new id
        __new_entity = self.DATABASE.Get_Entity(__key)(self.entity_free_id)
        self.entity_free_id += 1

        # set variables
        __new_entity.Set_Attrs(__attrs)

        # add new entity to the list
        self.entities.append(__new_entity)


    def Remove_Entity(self, __attrs:dict[str, Any], _all:bool=False) -> None:
        """Removes existing entity that has attribute values.
        \n If `all` is `True`, then all entities that fits will be removed. Only first one otherwise.
        """
        
        for __i in range(len(self.entities)):
            if self.entities[__i].Check_Attrs(__attrs):
                self.entities.remove(__i)
                if not _all: return


    def Get_Entity(self, __attrs:dict[str, Any], _all:bool=False) -> Entity|list[Entity]:
        """Returns existing entity that has attribute values.
        \n If `all` is `True`, then all entities that fits will be removed. Only first one otherwise.
        """

        if _all: __ret_list = list()

        for __entity in self.entities:
            if __entity.Check_Attrs(__attrs):
                if _all: __ret_list.append(__entity)
                else: return __entity
        
        if _all: return __ret_list
        else: return None


    # ----- Tiles functions -----
    def Tile_Create(self, __key:str, __attrs:dict[str, Any] = dict()) -> None:
        """Creates a Tile with given attrs added to default."""

        # create new and give it a new id
        __new_tile = self.DATABASE.Get_Tile(__key)(self.tiles_free_id)
        self.tiles_free_id += 1

        # set variables
        __new_tile.Set_Attrs(__attrs)

        # add new to the list
        self.tiles.append(__new_tile)


    def Remove_Tile(self, __attrs:dict[str, Any], _all:bool=False) -> None:
        """Removes existing tile that has attribute values.
        \n If `all` is `True`, then all tiles that fits will be removed. Only first one otherwise.
        """
        
        for __i in range(len(self.tiles)):
            if self.tiles[__i].Check_Attrs(__attrs):
                self.tiles.remove(__i)
                if not _all: return


    def Get_Tile(self, __attrs:dict[str, Any], _all:bool=False) -> Tile|list[Tile]:
        """Returns existing tile that has attribute values.
        \n If `all` is `True`, then all tiles that fits will be removed. Only first one otherwise.
        """

        if _all: __ret_list = list()

        for __tile in self.tiles:
            if __tile.Check_Attrs(__attrs):
                if _all: __ret_list.append(__tile)
                else: return __tile
        
        if _all: return __ret_list
        else: return None


