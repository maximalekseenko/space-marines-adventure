from data import Mission


class Mission1(Mission):
    KEY = "NLM1"

    MAP_SIZE = (7, 6)

    TILES = [
        ("NLTWall", {'x':0,'y':0}),
        ("NLTWall", {'x':1,'y':0}),
        ("NLTWall", {'x':2,'y':0}),
        ("NLTWall", {'x':3,'y':0}),
        ("NLTWall", {'x':4,'y':0}),
        ("NLTWall", {'x':5,'y':0}),
        ("NLTWall", {'x':6,'y':0}),
        
        ("NLTWall", {'x':0,'y':1}),
        ("NLTPortal", {'x':1,'y':1}),
        ("NLTPassage", {'x':2,'y':1}),
        ("NLTPortal", {'x':3,'y':1}),
        ("NLTWall", {'x':4,'y':1}),
        ("NLTConsole", {'x':5,'y':1}),
        ("NLTWall", {'x':6,'y':1}),

        ("NLTWall", {'x':0,'y':2}),
        ("NLTPassage", {'x':1,'y':2}),
        ("NLTWall", {'x':2,'y':2}),
        ("NLTPassage", {'x':3,'y':2}),
        ("NLTPassage", {'x':4,'y':2}),
        ("NLTPassage", {'x':5,'y':2}),
        ("NLTWall", {'x':6,'y':2}),

        ("NLTWall", {'x':0,'y':3}),
        ("NLTPassage", {'x':1,'y':3}),
        ("NLTPassage", {'x':2,'y':3}),
        ("NLTPassage", {'x':3,'y':3}),
        ("NLTWall", {'x':4,'y':3}),
        ("NLTPassage", {'x':5,'y':3}),
        ("NLTWall", {'x':6,'y':3}),
        
        ("NLTWall", {'x':0,'y':4}),
        ("NLTConsole", {'x':1,'y':4}),
        ("NLTWall", {'x':2,'y':4}),
        ("NLTPortal", {'x':3,'y':4}),
        ("NLTPassage", {'x':4,'y':4}),
        ("NLTPortal", {'x':5,'y':4}),
        ("NLTWall", {'x':6,'y':4}),
        
        ("NLTWall", {'x':0,'y':5}),
        ("NLTWall", {'x':1,'y':5}),
        ("NLTWall", {'x':2,'y':5}),
        ("NLTWall", {'x':3,'y':5}),
        ("NLTWall", {'x':4,'y':5}),
        ("NLTWall", {'x':5,'y':5}),
        ("NLTWall", {'x':6,'y':5}),
    ]

    ENTITIES = [
        ("NLEHeroBoltgun", {'x':0,'y':0}),
        ("NLTNecronWarrior", {'x':0,'y':0}),
        ("NLTNecronWarrior", {'x':0,'y':0}),
        ("NLTNecronWarrior", {'x':0,'y':0}),
    ]

