import pygame
from front.theatre import theatre
from engine import Act



class Act_Main(Act):
    def __init__(self) -> None:
        super().__init__()

        # scenes
        from .scene_main import Scene_Main
        self.scene_main = Scene_Main(self)
        from .scene_settings import Scene_Settings
        self.scene_settings = Scene_Settings(self)
        from .scene_connect import Scene_Connect
        self.scene_connect = Scene_Connect(self)

    
    def On_Update(self):
        self.scene_main.Update()
        self.scene_settings.Update()
        self.scene_connect.Update()


    def On_Open(self) -> None:
        self.scene_main.Open()
        self.scene_settings.Close()
        self.scene_connect.Close()
        self.Update()

    
    def On_Close(self) -> None:
        self.scene_main.Close()
        self.scene_settings.Close()
        self.scene_connect.Close()


    def On_Handle(self, event: pygame.event.Event) -> None:
        if self.scene_main.Handle(event): pass
        elif self.scene_settings.Handle(event): pass
        elif self.scene_connect.Handle(event): pass


    def On_Render(self) -> None:
        if self.scene_main.Render(): pass
        elif self.scene_settings.Render(): pass
        elif self.scene_connect.Render(): pass
