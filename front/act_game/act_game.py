import pygame
from front.theatre import theatre
from engine import Act



class Act_Game(Act):
    def __init__(self) -> None:
        super().__init__()

        # scenes

    
    def On_Update(self):
        pass


    def On_Open(self) -> None:
        pass

    
    def On_Close(self) -> None:
        pass


    def On_Handle(self, event: pygame.event.Event) -> None:
        pass


    def On_Render(self) -> None:
        self.surface.fill("#000000")
