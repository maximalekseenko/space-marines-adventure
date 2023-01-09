class DBItem:
    """Base class for other game components."""


    typecode = b'\x00'
    '''Code of this type.'''

    constvariables:dict[str, str | bool | int] = dict()
    '''Constant variables.'''
    paramvariables:dict[str, str | bool | int] = dict()
    '''Parameters varaibles.'''


    def Validate(self) -> bool:
        """Checks this dbitem for validation."""
        
        # variables are tested for being alpha-numberic + 
        # for variable in self.variables:
        #     if any(not __c.isa() and not __c.isspace() for __c in self.variables.items())
        return True


    def Encode(self) -> bytes:
        self.Validate()

        # 
        __ret_bytes = self.typecode

        __ret_bytes += b'\x1d'
        for __variable_item in self.constvariables.items():
            __ret_bytes += b'\x1e'
            __ret_bytes += __variable_item[0].encode('ascii')
            __ret_bytes += b'\x1f'
            __ret_bytes += __variable_item[1].encode('ascii')




