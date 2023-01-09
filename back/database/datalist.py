class Datalist:
    type:any
    '''Type of data in this data list.'''
    datas:list = list()
    '''List of data stored in this data list.'''


    def __init__(self, type) -> None:
        self.type = type


    def add(self, value):
        if value.TYPE != self.type: raise

        for data in self.datas:
            if data.KEY == value.KEY: raise

        self.datas.append(value)


    def rem(self, __value):
        """Remove value from data list."""

        # check type of the value
        if __value.TYPE != self.type: raise

        # search in datas for value
        for index in len(self.datas):

            if self.datas[index].KEY == __value.KEY:

                # remove it and return as function is complete
                self.datas.pop(index)
                return

        # raise as no valid value found in data
        raise


    def __getitem__(self, key):
        for data in self.datas:
            if data.KEY == key:
                return data
        return None


    def __repr__(self) -> str:
        ret_str = f"DataList<{self.type}>:"
        
        for data in self.datas:
            ret_str += '\n\t' + repr(data).replace('\n','\n\t')
        return ret_str