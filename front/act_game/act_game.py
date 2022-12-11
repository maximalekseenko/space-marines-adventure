import pygame
from front.theatre import theatre
from engine import Act



class Act_Game(Act):
    def __init__(self) -> None:
        super().__init__()

        # scenes

        from ..act_main.scene_main.element_button import Element_Button
        self.buttons = [
            Element_Button(self, "select A", lambda: theatre.client.Send({'name':"select", 'value':"A"})),
            Element_Button(self, "select B", lambda: theatre.client.Send({'name':"select", 'value':"B"})),
            Element_Button(self, "select C", lambda: theatre.client.Send({'name':"select", 'value':"C"})),
            Element_Button(self, "select D", lambda: theatre.client.Send({'name':"select", 'value':"D"}))]

    
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
        self.Update()

    
    def On_Close(self) -> None:
        pass


    def On_Handle(self, event: pygame.event.Event) -> None:
        for button in self.buttons: button.Handle(event)


    def On_Render(self) -> None:
        self.surface.fill("#000000")

        for button in self.buttons: button.Render()
