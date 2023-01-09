# from back.database import database

# database.Import('data/necron_labyrinth/')

# # print(repr(database))

# print(database['T']['NL_TW'])


import back


from data import necron_labyrinth
back.db.Import(necron_labyrinth)

m = back.db.Get_Mission("NLM1")(None)




print(m)

# Mission1(None)
