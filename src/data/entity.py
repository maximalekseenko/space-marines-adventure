class Entity:
    KEY:str = ""

    IMAGE:str = None
    '''Default image key. \n\n Export/Import parameter.'''
    VARIABLES:dict[str, any] = {
        'x': 0,
        'y': 0,
    }
    '''Default variables. \n\n Export/Import parameter.'''


    def __init__(self, __id:int) -> None:
        self.id = __id

        self.image:str = ""
        '''Current image. \n\n Do not edit directly! Use corresponding functions!'''

        self.variables:dict[str, any] = dict()
        '''Current variables. \n\n Do not edit directly! Use corresponding functions!'''

        # set defaults
        for __key, __value in self.VARIABLES.items():
            self.Variables_Set(__key, __value)

    
    def __abs_repr__(self) -> str:
        ret_str =  f"Entity(abstract):"
        ret_str += f"\n├key: {self.KEY}"
        ret_str += f"\n├variables: {self.VARIABLES}"
        ret_str += f"\n├image: {self.IMAGE}"
        return ret_str


    def __repr__(self) -> str:
        ret_str =  f"Entity:"
        ret_str += f"\n├key: {self.KEY}"
        ret_str += f"\n├id: {self.id}"
        ret_str += f"\n├variables: {self.variables}"
        ret_str += f"\n├image: {self.image}"
        return ret_str

    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}:{self.id}[{self.variables['x']}:{self.variables['y']}]"

    
    # variables
    def Variables_Set(self, __key:str, __value:any) -> None:
        """Sets variable."""

        self.variables[__key] = __value


    def Variables_Get(self, __key:str) -> None:
        """Sets variable."""

        return self.variables.get(__key, None)