from data.database import DataBase

database = DataBase()


from data.packs import necron_labyrinth
database.Import(necron_labyrinth.ASSETS)


mission = database.Get_Mission("NLM1")(None)


def map():
    for x in range(mission.MAP_SIZE[0]):
        for y in range(mission.MAP_SIZE[1]):
            char = ' '

            entity = mission.Get_Entity({'x': x, 'y': y})
            tile = mission.Get_Tile({'x': x, 'y': y})

            if entity:
                if entity.Check_Attr('hero', True): char = '✠'
                elif entity.Check_Attr('enemy', True): char = '☠'
            elif tile:
                if tile.Check_Attr('wall', True): char = '█'
                elif tile.Check_Attr('console', True): 
                    if tile.Check_Attr('active', True):
                        char = '▣'
                    else: char = '□'
                elif tile.Check_Attr('portal', True): char = '◌'

            print(char, end='')
        print()

map()
print()

positions = [0,1,2,3]

import random
random.shuffle(positions)

portals = mission.Get_Tile({'portal': True}, _all=True)

for enemy in mission.Get_Entity({'enemy': True}, _all=True):
    portal = portals[positions.pop()]
    enemy.Set_Attrs({'x': portal.Get_Attr('x'), 'y': portal.Get_Attr('y')})


hero = mission.Get_Entity({'hero':True})
portal = portals[positions.pop()]
hero.Set_Attrs({'x': portal.Get_Attr('x'), 'y': portal.Get_Attr('y')})

map()

