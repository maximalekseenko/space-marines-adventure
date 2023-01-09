from data.database import DataBase

database = DataBase()


from data.packs import necron_labyrinth
database.Import(necron_labyrinth.ASSETS)


mission = database.Get_Mission("NLM1")(None)


# print(mission)

for row in mission.tile_grid:
    print(''.join(['.' if tiles.__len__() == 0 else 'X' if tiles[0].Variables_Get('wall') else ' ' for tiles in row]))
 