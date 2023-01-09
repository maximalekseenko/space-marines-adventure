from data import Entity


class Entity_HeroChainsword(Entity):
    KEY = "NLEHeroChainsword"
    VARIABLES = {
        'range':4,
        'actions':4,
        'hero':True,
    }

class Entity_HeroBoltgun(Entity):
    KEY = "NLEHeroBoltgun"
    VARIABLES = {
        'range':6,
        'actions':4,
        'hero':True,
    }


class Entity_HeroFlamer(Entity):
    KEY = "NLTHeroFlamer"
    VARIABLES = {
        'range':3,
        'actions':3,
        'hero':True,
    }

class Entity_NecronWarrior(Entity):
    KEY = "NLTNecronWarrior"
    VARIABLES = {
        'enemy':True,
    }