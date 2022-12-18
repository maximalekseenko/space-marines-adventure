import pygame
from front.theatre import theatre
from engine import Scene



class Scene_Connect(Scene):
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
        if theatre.client.Connect():
            from front.act_game import Act_Game
            theatre.current_act = Act_Game()


