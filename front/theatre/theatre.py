from engine import Theatre



class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()
        
        self.SERVER_ADDRESS = ("0.0.0.0", 5555)

        from .client import Client
        self.client = Client(self.SERVER_ADDRESS)



theatre = Theatre()