from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: from .hero import Hero




class Equipment:
    """Supply, atrefacts, doctrines, ect. that heroes can carry.
    \n Representation of `secial` cards in original game.
    """

    NAME:str = ""


    def __init__(self, hero:Hero) -> None:
        self.hero = hero


    def Use(self, target) -> bool:
        """Use this equipt at the `target`."""

        if not self.hero.Move(target): return False

        self.Discard()

        return True



    def Discard(self) -> None:
        """Remove this equipt from hero's inventory."""

        self.hero.equipment.remove(self)

