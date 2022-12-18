from __future__ import annotations
from .campaign import Campaign
from .player import Player



class Game:
    """Object for handling connections, campaigns, ect."""
    def __init__(self, id:int, settings:dict) -> None:
        self.id:int = id
        self.settings = settings

        self.campaign:Campaign = Campaign(self)
        '''Currently ongoing camaign.'''

        self.players:list[Player] = list()
        '''List of players in this game.'''



    def Validate_Settings(self, settings):
        """Validate if given `settings` fits to the current settings in this game."""
        # TODO: CODE
        return True


    def Handle(self, address:tuple, request:dict) -> None:
        """Handle user `request` by their `address`."""

        # join - add/move address to the corresponding list
        if request['name'] == "join":
            self.Join(address, request['value'])
            
        elif request['name'] == "select":
            print(request['value'])

    
    def Join(self, address:tuple, dest:str) -> None:
        """Add/move `address` to the list, specified by `dest`:
        *   `"player"` - join as player. join nothing if cannot add to players.
        *   `"AAA"` - join as AAA. 
        *   `"any"` - join as players. join AAA if cannot add to players.
        """

        # join as player
        if dest == "any" or dest == "player":
            for player in self.players:
                if player.address == address:
                    return

            # TODO: check for presence in other

            # add address to players
            self.players.append(Player(self, address))
        


    def Get_Data(self, address:tuple) -> dict:
        """Get data for the local game of the player by player's `address`."""
        # return {
        #     'players': [player.address for player in self.players],
        # }
        return {
            'stage_type': "selection",
            'title':        "AAA",
            'description':  "AAAAAA AAA AAAAA",
            'options':      [
                ['text aaa', 'a', 'a.png', True, []],
                ['text bbb', 'b', 'b.png', True, []],
                ['text ccc', 'c', 'c.png', False, []],
                ['text ddd', 'd', 'd.png', True, []],
            ],
        }