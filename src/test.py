from data.database import DataBase

database = DataBase()


from data.packs import necron_labyrinth
database.Import(necron_labyrinth.ASSETS)


mission = database.Get_Mission("NLM1")(None)


# print(mission)

for x in range(mission.MAP_SIZE[0]):
    print()
    for y in range(mission.MAP_SIZE[1]):
        char = ' '

        entity = mission.Entity_Get_By_Position(x, y)
        tile = mission.Tile_Get_By_Position(x, y)

        if entity:
            if entity.Variables_Get('hero') == True: char = '✠'
            elif entity.Variables_Get('enemy') == True: char = '💀'
        elif tile:
            if tile.Variables_Get('wall') == True: char = '█'
            elif tile.Variables_Get('console') == True: 
                if tile.Variables_Get('active'):
                    char = '▣'
                else: char = '□'
            elif tile.Variables_Get('portal') == True: char = '◌'

        print(char, end='')

print()