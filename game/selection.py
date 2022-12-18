from .player import Player


class Selection:
    """Stage where heroes select something (e.g. equiptment, mission, map, ect.).
    \n ---
    \n parameters:
    * `TITLE`
    * `DESCRIPTION`
    * `OPTIONS`
    \n ---
    \n functions:
    * `On_Start`
    * `Get_Title`
    * `Get_Description`
    * `Get_Options`
    """

    TITLE: str
    '''Title that shows on top of this selection.'''

    DESCRIPTION: str
    '''Text that explains what the selection is about.'''

    OPTIONS: list[tuple[str, str, str, list[Player]]]
    '''Options to select from. \n\n `option_key`, `image_key`, `description`, `selected_by`'''

    
    def __init__(self, campaign) -> None:
        self.campaign = campaign

        self.selected_values: dict[list]
        

    
    def On_Start(self, player: Player, option_key: str) -> None:
        """"""


    def On_Select(self, player: Player, option_key: str) -> None:
        """"""
  

    def On_Deselect(self, player: Player, option_key: str) -> None:
        """"""


    def Get_Data(self, player: Player, option_key: str) -> dict[str, str | list[tuple[str, str, bool]]]:
        """Returns data for giving `player`
        * `'title'`: `str` # title of this selection
        * `'description'`: `str` # description of this selection
        * `'options'`: `list[tuple[str, str, bool]]` # list of options to select as tuples of image_key, description, is_selectable
        """

        return {
            'title':        self.Get_Title(player),
            'description':  self.Get_Description(player),
            'options':      self.Get_Options(player),
        }

        
    def Get_Title(self, player: Player, option_key: str) -> str:
        """Get title for data for `player`."""
        return self.TITLE


    def Get_Description(self, player: Player, option_key: str) -> str:
        """Get description for data for `player`."""
        return self.DESCRIPTION


    def Get_Options(self, player: Player, option_key: str) -> list[tuple[str, str, list[Player], bool]]:
        """Get options for data for `player`."""
        return [(
            option[1],
            option[2],
            option[3],
            len(option[3]) == 0)

            for option in self.OPTIONS]