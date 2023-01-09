from engine import Theatre



class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()

        self.path_to_output_dir = "../"



theatre = Theatre()