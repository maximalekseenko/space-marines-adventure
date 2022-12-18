from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING: from .campaign import Campaign



class Mission:
    KEY:str = ""

    def __init__(self, campaign:Campaign) -> None:
        self.campaign = campaign


        self.stage:str

        self.Start_Preparation()


    def Start_Preparation(self):
        self.stage = "preparation"


    def Get_Data(self):
        return {
            "mission_key": self.KEY,
            "stage": self.stage,
        }


    def Handle_Hero_Request(self, request:dict):
        if self.stage == "preparation":
            self.Handle_Hero_Preparation(request)


    def _Handle_Hero_Preparation(self, request:dict):
        if request['type'] == "select":
            pass