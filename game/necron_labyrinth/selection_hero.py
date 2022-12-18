from ..selection import Selection



class Selection_Hero(Selection):
    TITLE = "Select Hero"

    DESCRIPTION = ""

    OPTIONS = [
        ('hero1', 'hero1.png', "Hero1", list()),
        ('hero2', 'hero2.png', "Hero2", list()),
        ('hero3', 'hero3.png', "Hero3", list()),
        ('hero4', 'hero4.png', "Hero4", list()),
        ('hero5', 'hero5.png', "Hero5", list()),
    ]


    # def On_Start(self) -> None:
    #     from ..hero import Hero
    #     self.values = [
    #         Hero(6,4),
    #         Hero(5,5),
    #         Hero(4,6),
    #         Hero(3,7),
    #         Hero(2,8),
    #     ]