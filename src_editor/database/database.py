import os



class Database:
    """DB
    \n ---
    \n When exported as datafile, has next file structure:
    * `SOH` `<db name>`
    \n for each item in database:
    * `FS` `<item type code>`
    * `GS`; for each const variable in item:
    * `RS` `<const variable name>` `US` `<const variable value>`
    * `GS`; for each param variable in item:
    * `RS` `<const variable name>`
    \n at the end of file:
    * `EOT`
    """
    def __init__(self) -> None:
        self.items = list()
        '''Items'''

    
    def Export(self, __path:str, __name:str, _additive:bool=True, _additive_overwrite:bool=True) -> None:
        """Export database from `.df` file by given path with given name.
        *  If additive parameter is `True` will add current data in database will be added into file, elsewise will just replace original file with a new one.
        *  If additive overwrite parameter is `True` will write over existing data in file, elsewise will add only new data to the file.
        """

        # validate parameters
        ## __path
        if not os.path.exists(os.path.dirname(__path)): raise NotADirectoryError("Cannot export database due to incorrect path.")
        if os.path.isfile(__path) and _additive: 
            pass # TODO warn
            if _additive_overwrite: 
                pass # TODO warn x2
        ## __name
        if any(not __c.isalpha() and not __c.isspace() for __c in __name): raise ValueError("Cannot export database due to incorrect name.")

        # import data from file
        if _additive: self.Import(__path, _overwrite=not _additive_overwrite)

        # export
        with open(__path, 'wb') as __file:

            # write start of datafile
            __file.write(b'\x01')

            # write name
            __file.write(__name.encode('ascii'))

            # write data
            for item in self.items:
                __file.write(b'\x1c')
                # TODO this

            # write end of datafile
            __file.write(b'\x04')


    def Import(self, __path:str, _overwrite:bool=True, _clean:bool=False) -> None:
        """Import database as `.df` file by given path.
        * If overwrite parameter is `True`, imported data from file, that already exists will overwrite data present in database, discarded elsewise.
        * If clean parameter is `True`, Database will clean before import.
        """
        pass
