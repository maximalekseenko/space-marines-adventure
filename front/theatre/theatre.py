from engine import Theatre
import pygame


class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()
        
        self.SERVER_ADDRESS = ("0.0.0.0", 5555)

        self.FONT_OLDENGLISHTEXTMT_30 = pygame.font.Font("oldenglishtextmt.ttf", 30)
        self.FONT_OLDENGLISHTEXTMT_12 = pygame.font.Font("oldenglishtextmt.ttf", 12)
        self.FONT_OLDENGLISHTEXTMT_45 = pygame.font.Font("oldenglishtextmt.ttf", 45)

        from .client import Client
        self.client = Client(self.SERVER_ADDRESS)

        # /TODO DELETE\
        from back.database import database
        database.Import('data/necron_labyrinth/')
        # \TODO DELETE/



theatre = Theatre()