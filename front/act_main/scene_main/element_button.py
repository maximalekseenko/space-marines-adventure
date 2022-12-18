import pygame
from front.theatre import theatre
from engine import Element



class Element_Button(Element):
    def __init__(self, scene, text:str, onclick) -> None:
        super().__init__(scene, None, pygame.SRCALPHA)

        self.text = text
        self.onclick = onclick

        self.is_highlighted = False

        self.text_surface = pygame.Surface((0,0))
        self.text_rect = pygame.Rect(0,0,0,0)
        self.text_font = theatre.FONT_OLDENGLISHTEXTMT_30


    def On_Update(self):
        self.text_surface = self.text_font.render(self.text, 1, "#0a0a0a")
        self.text_rect = self.text_surface.get_rect(center = self.surface.get_rect().center)

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(event.pos)

        # click
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
            self.onclick()

    
    def On_Render(self) -> None:
        # background
        if self.is_highlighted:
            pygame.draw.rect(self.surface, "#a0a0a0", self.surface.get_rect(), 0, 3)
        else:
            pygame.draw.rect(self.surface, "#c0c0c0", self.surface.get_rect(), 0, 3)

        # text
        self.surface.blit(self.text_surface, self.text_rect)

        # final
        self.scene.surface.blit(self.surface, self.rect)