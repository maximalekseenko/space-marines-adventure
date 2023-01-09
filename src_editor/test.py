# from theatre import theatre

# from act_edit import Act_edit
# theatre.current_act = Act_edit("../test.df")

# theatre.Begin()


from database import Database

db = Database()

db.Export('../test.df', 'test')
