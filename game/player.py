from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: from .game import Game



class Player:

    def __init__(self, game:Game, address:str) -> None:
        self.game:Game = game
        self.address:str = address