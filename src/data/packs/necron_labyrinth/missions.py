from data import Mission


class Mission1(Mission):
    KEY = "NLM1"

    MAP_SIZE = (7, 6)

    TILES = [
        ("NLTW", {'x':0,'y':0}),
        ("NLTW", {'x':1,'y':0}),
        ("NLTW", {'x':2,'y':0}),
        ("NLTW", {'x':3,'y':0}),
        ("NLTW", {'x':4,'y':0}),
        ("NLTW", {'x':5,'y':0}),
        ("NLTW", {'x':6,'y':0}),
        
        ("NLTW", {'x':0,'y':1}),
        ("NLTP", {'x':1,'y':1}),
        ("NLTP", {'x':2,'y':1}),
        ("NLTP", {'x':3,'y':1}),
        ("NLTW", {'x':4,'y':1}),
        ("NLTW", {'x':5,'y':1}),
        ("NLTW", {'x':6,'y':1}),

        ("NLTW", {'x':0,'y':2}),
        ("NLTP", {'x':1,'y':2}),
        ("NLTW", {'x':2,'y':2}),
        ("NLTP", {'x':3,'y':2}),
        ("NLTP", {'x':4,'y':2}),
        ("NLTP", {'x':5,'y':2}),
        ("NLTW", {'x':6,'y':2}),

        ("NLTW", {'x':0,'y':3}),
        ("NLTP", {'x':1,'y':3}),
        ("NLTP", {'x':2,'y':3}),
        ("NLTP", {'x':3,'y':3}),
        ("NLTW", {'x':4,'y':3}),
        ("NLTP", {'x':5,'y':3}),
        ("NLTW", {'x':6,'y':3}),
        
        ("NLTW", {'x':0,'y':4}),
        ("NLTW", {'x':1,'y':4}),
        ("NLTW", {'x':2,'y':4}),
        ("NLTP", {'x':3,'y':4}),
        ("NLTP", {'x':4,'y':4}),
        ("NLTP", {'x':5,'y':4}),
        ("NLTW", {'x':6,'y':4}),
        
        ("NLTW", {'x':0,'y':5}),
        ("NLTW", {'x':1,'y':5}),
        ("NLTW", {'x':2,'y':5}),
        ("NLTW", {'x':3,'y':5}),
        ("NLTW", {'x':4,'y':5}),
        ("NLTW", {'x':5,'y':5}),
        ("NLTW", {'x':6,'y':5}),
    ]

    ENTITIES = []
