from .mission import Mission
from .selection import Selection

TYPESTAGE = Mission|Selection


class Campaign:
    """Core of the gameplay. \n\n Handles player acrtions, missions and selections."""


    def __init__(self, game) -> None:
        self.game = game

        self.stages:list[type[TYPESTAGE]] = list()
        '''List of all stages present in this campaign.'''

        self.players_max = 4
        self.heroes:list = list()

        self.current_stage_index = -1
        self.current_stage:TYPESTAGE


    def get_stage() -> TYPESTAGE:
        pass


    def Stage_Next(self) -> None:
        current_stage_index = 0

    def Stage_Get_Current(self) -> TYPESTAGE:
        """Get current stage."""
        return self.current_stage

    def Finish_Victory(self):...
    def Finish_Failure(self):...