import pygame
from front.theatre import theatre
from engine import Act



class Act_Game(Act):
    def __init__(self) -> None:
        super().__init__()

        # scenes
        from .scene_selection import Scene_Selection
        self.scene_selection = Scene_Selection(self)


        self.current_stage_type = None

        theatre.client.Handle_Request = self.Handle_Data_From_Server

        theatre.client.Send({'name':"update"})


    def Handle_Data_From_Server(self, data:dict):
        if data['stage_type'] == "selection":
            if self.current_stage_type == data['stage_type']:

                # set data
                self.scene_selection.Set_Data(data)

            else:
                # set current stage type
                self.current_stage_type = data['stage_type']

                # open/close scenes
                self.scene_selection.Open()

                # set data
                self.scene_selection.Set_Data(data)

    
    def On_Update(self):
        self.scene_selection.Update()


    def On_Open(self) -> None:
        self.scene_selection.Close()

        # update
        self.Update()

    
    def On_Close(self) -> None:
        self.scene_selection.Close()


    def On_Handle(self, event: pygame.event.Event) -> None:
        if self.scene_selection.Handle(event): return


    def On_Render(self) -> None:
        self.surface.fill("#000000")

        if self.scene_selection.Render(): return
