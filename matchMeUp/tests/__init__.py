from pony.orm import Database

db = Database('sqlite', ':memory:', create_db=True)
