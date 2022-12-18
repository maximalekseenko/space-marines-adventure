import pygame
from front.theatre import theatre
from engine import Scene
from .element_optionbutton import Element_OptionButton



class Scene_Selection(Scene):
    """Scene for campaign stage where player need to select something (e.g. equipment or heroes)."""

    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        # for snippets
        from ..act_game import Act_Game
        self.act:Act_Game


        self.optionbuttons:list[Element_OptionButton] = list()


    def Set_Data(self, data:dict):
        """Set data for selection."""

        self.optionbuttons.clear()

        for option in data['options']:
            self.optionbuttons.append(Element_OptionButton(self, *option))

        self.Update()


    def On_Update(self):
        BUTTONS_TOP = 100
        BUTTON_STEP = 10
        BUTTON_SIZE = [100,25]
        BUTTON_CENTEX = self.surface.get_width() / 2

        for i_optionbutton in range(len(self.optionbuttons)):
            self.optionbuttons[i_optionbutton].rect = pygame.Rect(0, 0, *BUTTON_SIZE)
            self.optionbuttons[i_optionbutton].rect.centery = i_optionbutton * (BUTTON_SIZE[1] + BUTTON_STEP) + BUTTONS_TOP
            self.optionbuttons[i_optionbutton].rect.centerx = BUTTON_CENTEX

            self.optionbuttons[i_optionbutton].Update()


    def On_Open(self) -> None:
        pass


    def On_Close(self) -> None:
        pass

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        for button in self.optionbuttons: button.Handle(event)


    def On_Render(self) -> None:
        self.surface.fill("#0a0a0a")

        for button in self.optionbuttons: button.Render()

        # self.act.surface.blit()