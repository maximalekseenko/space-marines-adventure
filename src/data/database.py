# import os
from .tile import Tile
from .mission import Mission
from .entity import Entity



class DataBase:
    """Class that witholds all data."""

    def __init__(self) -> None:
        self.list_tile:list[type[Tile]] = list()
        '''List of tiles located in database. \n\n Do not access direcly! Use corresponding functions!'''
        self.list_mission:list[type[Mission]] = list()
        '''List of missions located in database. \n\n Do not access direcly! Use corresponding functions!'''
        self.list_entity:list[type[Entity]] = list()
        '''List of entities located in database. \n\n Do not access direcly! Use corresponding functions!'''


    def Import(self, __assets:list[type[Tile]|type[Mission]|type[Entity]]):
        for __asset in __assets: 
            if Tile in __asset.mro(): self.Import_Tile(__asset)
            elif Mission in __asset.mro(): self.Import_Mission(__asset)
            elif Entity in __asset.mro(): self.Import_Entity(__asset)


    # ----- List imports -----
    def Import_Tile(self, __asset:type[Tile]) -> None:
        """Imports tile to the database."""

        # validate
        if Tile not in __asset.mro(): raise TypeError("Attempt to import of incorrect type.")

        # set database
        __asset.DATABASE = self

        # add
        self.list_tile.append(__asset)


    def Import_Mission(self, __asset:type[Mission]) -> None:
        """Imports mission to the database."""

        # validate
        if Mission not in __asset.mro(): raise TypeError("Attempt to import of incorrect type.")

        # set database
        __asset.DATABASE = self

        # add
        self.list_mission.append(__asset)


    def Import_Entity(self, __asset:type[Entity]) -> None:
        """Imports entity to the database."""

        # validate
        if Entity not in __asset.mro(): raise TypeError("Attempt to import of incorrect type.")

        # set database
        __asset.DATABASE = self

        # add
        self.list_entity.append(__asset)


    # ----- List gets -----
    def Get_Tile(self, __key:str) -> type[Tile]:
        """Returns tile type from database by given key."""

        for __asset in self.list_tile:
            if __asset.KEY == __key:
                return __asset


    def Get_Mission(self, __key:str) -> type[Mission]:
        """Returns mission type from database by given key."""

        for __asset in self.list_mission:
            if __asset.KEY == __key:
                return __asset


    def Get_Entity(self, __key:str) -> type[Entity]:
        """Returns tile type from database by given key."""

        for __asset in self.list_entity:
            if __asset.KEY == __key:
                return __asset


    # def Import(self, path:str):
    #     """Imports data by given `path`.
    #     \n If given path is a file, imports that file;
    #     \n If given path is a filder, imports all files in that folder with deepness of 1.
    #     """

    #     if os.path.isdir(path):
    #         for sub_path in os.listdir(path):
    #             self.Import(os.path.join(path, sub_path))
            
    #     if os.path.isfile(path):
    #         self._Import_File(path)
    

    # def _Import_File(self, path):
    #     """Imports a file by given `path`."""

    #     pass


    # def _Import_Campaign(self, path):
    #     try: 
    #         file = open(path)

            

    #         file.close()
    #     except:
    #         print("importerror")


    def __repr__(self) -> str:
        ret_str = f"DataBase:"
        ret_str += f"\n├list-tile ({len(self.list_tile)}):"
        for __asset in self.list_tile: ret_str += "\n│├" + __asset.__abs_repr__(__asset).replace('\n','\n││')
        ret_str += f"\n├list-mission ({len(self.list_mission)}):"
        for __asset in self.list_mission: ret_str += "\n│├" + __asset.__abs_repr__(__asset).replace('\n','\n││')
        return ret_str