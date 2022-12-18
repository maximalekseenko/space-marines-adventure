from .equipment import Equipment


class Hero:

    def __init__(self, ACTIONS:int=4, RANGE:int=6, icon=None) -> None:
        self.ACTIONS = ACTIONS
        self.RANGE = RANGE

        self.wounds_max = 2
        self.wounds = 2

        self.equipment_max = 2
        self.equipment:list[Equipment] = 0


    def Add_Equiptment(self, equipment:Equipment) -> bool:
        """Add given `equipment` to the hero's inventory.
        \n Returns `False` if failed to add.
        \n Returns `True` if succeeded
        """

        # check if can add
        ## inventory size
        if len(self.equipment) + 1 > self.equipment_max: return False

        # add
        self.equipment.append(equipment)

        # return
        return True


    def Move(self, target):
        pass