import pygame
from front.theatre import theatre
from engine import Scene



class Scene_Settings(Scene):
    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)


    def On_Update(self):
        pass


    def On_Open(self) -> None:
        pass


    def On_Close(self) -> None:
        pass

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        pass


    def On_Render(self) -> None:
        pass


