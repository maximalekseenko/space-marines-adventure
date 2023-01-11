from __future__ import annotations
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING: 
    from .database import DataBase
    from .mission import Mission


class Entity:
    KEY:str = ""
    '''Key for finding this Entity in database'''

    ATTRS:dict[str, Any] = {
        'id': -1,
        'x': 0,
        'y': 0,
        'image': '',
    }
    '''Default attributes and their values, that applied upon creation.
    \n Default attrs for any Entity are:
    * `id` - `int` identification number. Setted on creation. Constant.
    * `x` - `int` horizontal location on map.
    * `y` - `int` vertical location on map.
    * `image` - `str` key of image to display.
    * 'hero' - `bool` used to determine if this entity is a hero.
    * 'enemy' - `bool` used to determine if this entity is an enemy.
    '''

    EVENTS:dict[str, function] = dict()


    def __init__(self, __mission:Mission) -> None:

        self.mission = __mission

        self.attrs:dict[str, Any] = dict()
        '''Attributes that this Entity has.'''

        self.events:dict[str, function] = dict()

        # set defaults
        ## attrs
        self.Set_Attrs(self.ATTRS)

        ## events
        for __key, __value in self.EVENTS.items():
            self.events[__key] = getattr(self, __value)


    def __repr__(self) -> str:
        ret_str =  f"<{self.__class__.__name__} {self.attrs}>"
        return ret_str

    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


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


    # Events
    def Event(self, __key:str, __args:list):
        __event = self.events.get(__key, None)
        if __event: __event()
