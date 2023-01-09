from engine import Act
from database import Database



class Act_Edit(Act):
    def __init__(self, __path_to_datafile) -> None:
        super().__init__()

        self.path_to_datafile = __path_to_datafile
        '''Path to file for current edit. \n\n Used for reading/wrighting.'''

        self.database = Database()
        '''Temporary database for editing.'''