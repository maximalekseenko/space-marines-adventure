from data import Entity


class Entity_HeroChainsword(Entity):
    KEY = "NLEHeroChainsword"
    DEFAULT_ATTRS = {
        'range':4,
        'actions':4,
        'hero':True,
    }

class Entity_HeroBoltgun(Entity):
    KEY = "NLEHeroBoltgun"
    DEFAULT_ATTRS = {
        'range':6,
        'actions':4,
        'hero':True,
    }


class Entity_HeroFlamer(Entity):
    KEY = "NLTHeroFlamer"
    DEFAULT_ATTRS = {
        'range':3,
        'actions':3,
        'hero':True,
    }

class Entity_NecronWarrior(Entity):
    KEY = "NLTNecronWarrior"
    DEFAULT_ATTRS = {
        'enemy':True,
    }