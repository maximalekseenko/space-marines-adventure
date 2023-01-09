import os


class Parser:
    _SYMSPACE = [' ', '\n']
    _SYMBRACEOPEN = ['[', '(', '{', '<']
    _SYMBRACECLOSE = [']', ')', '}', '>']
    _SYMIGNOREOPEN = ['', '#']
    _SYMIGNORECLOSE = ['', '#', '\n']
    _SYMWORDOPEN = ['"', '\'']
    _SYMWORDCLOSE = ['"', '\'']


    def __init__(self) -> None:
        pass


    def parse(self, path) -> dict:
        """Parse file at given `path`."""

        # check if file
        if not os.path.isfile(path): return False

        # read file
        with open(path) as file:
            data = file.read()

        # parse
        data = list(self._clean_file(data))
        data = self.parse_data(data)
        from pprint import pprint
        pprint(data)

        # return self._parsed_data

    
    def _clean_file(self, data:str) -> list:
        clean_data = list()

        word = ""

        is_wording = False
        is_ignoring = False

        for sym in data:
            # symbol is wording
            if sym in self._SYMWORDOPEN and not is_wording:
                is_wording = True
                word += self._SYMWORDOPEN[0]
            elif sym in self._SYMWORDCLOSE and is_wording:
                is_wording = False
                word += self._SYMWORDCLOSE[0]
            elif is_wording:
                word += sym

            # symbol is ignore
            elif sym in self._SYMIGNOREOPEN and not is_ignoring:
                is_ignoring = True
            elif sym in self._SYMIGNORECLOSE and is_ignoring:
                is_ignoring = False
            elif is_ignoring: continue

            # symbol is brace
            elif sym in self._SYMBRACEOPEN:
                if word:
                    yield word
                    word = ""
                yield self._SYMBRACEOPEN[0]
            elif sym in self._SYMBRACECLOSE:
                if word:
                    yield word
                    word = ""
                yield self._SYMBRACECLOSE[0]
            
            # symbol is space
            elif sym in self._SYMSPACE:
                if word:
                    yield word
                    word = ""

            # sym is word
            else: 
                word += sym


        if word:
            yield word


    def parse_data(self, data:list) -> list:
        parsed_data = list()
        

        index = 0
        while index != len(data) - 1:

            
            index += 1
                
        return parsed_data

p = Parser()
print(p.parse("../../data/necron_labyrinth/hero.select"))
