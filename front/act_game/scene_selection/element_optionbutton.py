import pygame
from front.theatre import theatre
from engine import Element



class Element_OptionButton(Element):
    def __init__(self, scene, text:str, option_key:str, image_key:str, is_selectable:bool, selected_by:list) -> None:
        super().__init__(scene, None, pygame.SRCALPHA)

        self.text:str = text
        '''Text on this option. \n\n Do not forget `.Update()` this button on change.'''

        self.option_key:str = option_key
        '''Key of option this button represents. \n\n Used for backend determine what option this is.'''

        self.image_key:str = image_key
        '''Key of an image this button should use.'''

        self.is_selectable:bool = is_selectable
        '''Is this client bears an ability to select this option.'''

        self.selected_by:list = selected_by
        '''List of thouse, who selected this option.'''

        self.is_highlighted = False

        self.text_surface = pygame.Surface((0,0))
        self.text_rect = pygame.Rect(0,0,0,0)
        self.text_font = theatre.FONT_OLDENGLISHTEXTMT_30


    def On_Update(self):
        self.text_surface = self.text_font.render(self.text, 1, "#0a0a0a")
        self.text_rect = self.text_surface.get_rect(center = self.surface.get_rect().center)

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        if not self.is_selectable: return

        # highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(event.pos)

        # click
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and event.button == 1:
            theatre.client.Send({'name':"select", 'value':self.option_key})

    
    def On_Render(self) -> None:
        # background
        if not self.is_selectable:
            pygame.draw.rect(self.surface, "#505050", self.surface.get_rect(), 0, 3)
        elif self.is_highlighted:
            pygame.draw.rect(self.surface, "#a0a0a0", self.surface.get_rect(), 0, 3)
        else:
            pygame.draw.rect(self.surface, "#c0c0c0", self.surface.get_rect(), 0, 3)

        # text
        self.surface.blit(self.text_surface, self.text_rect)

        # final
        self.scene.surface.blit(self.surface, self.rect)