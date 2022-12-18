class Campaign:
    """Core of the gameplay. \n\n Handles player acrtions, missions and selections."""


    def __init__(self, game) -> None:
        self.game = game

        self.players_max = 4
        self.heroes:list = list()

        self.active_stage:Mission|Selection


    def New(self):
        pass
