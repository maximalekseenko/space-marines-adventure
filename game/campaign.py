class Campaign:
    def __init__(self, game) -> None:
        self.game = game
        self.stage = 0
        '''
        \n 0 - None
        \n 1 - Select for mission 1
        \n 1.5 - Mission 1
        \n 2 - Select for mission 2
        \n 2.5 - Mission 2
        \n 3 - Select for mission 3
        \n 3.5 - Mission 3
        '''

        from .hero import Hero
        self.heroes = [
            Hero(4,6),
            Hero(4,6),
            Hero(4,6),
            Hero(4,6),
            Hero(4,6)]

        self.selected_heroes = []


    def Get_Stage_Type():
        pass


    def Handle_Select(self, player, i_selection):
        if self.stage == 1:
            pass



    def New(self):
        self.stage = 1

    
