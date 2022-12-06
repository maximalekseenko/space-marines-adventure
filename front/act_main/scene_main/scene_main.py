import pygame
from front.theatre import theatre
from engine import Scene



class Scene_Main(Scene):
    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        from ..act_main import Act_Main
        self.act:Act_Main

        # buttons
        from .element_button import Element_Button
        self.buttons = [
            Element_Button(self, "connect", self._button_onclick_connect),
            Element_Button(self, "settings", self._button_onclick_settings),
            Element_Button(self, "exit", self._button_onclick_exit),
            ]


    def On_Update(self):
        BUTTONS_TOP = 100
        BUTTON_STEP = 10
        BUTTON_SIZE = [100,25]
        BUTTON_CENTEX = self.surface.get_width() / 2

        for i_button in range(len(self.buttons)):
            self.buttons[i_button].rect = pygame.Rect(0, 0, *BUTTON_SIZE)
            self.buttons[i_button].rect.centery = i_button * (BUTTON_SIZE[1] + BUTTON_STEP) + BUTTONS_TOP
            self.buttons[i_button].rect.centerx = BUTTON_CENTEX

            self.buttons[i_button].Update()


    def On_Open(self) -> None:
        pass


    def On_Close(self) -> None:
        pass

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        for button in self.buttons: button.Handle(event)


    def On_Render(self) -> None:
        self.surface.fill("#0a0a0a")

        for button in self.buttons: button.Render()


    def _button_onclick_connect(self):
        self.act.scene_connect.Open()
        self.Close()


    def _button_onclick_settings(self):
        self.act.scene_settings.Open()
        self.Close()


    def _button_onclick_exit(self):
        theatre.is_running = False
