'''
Created on Jun 26, 2015

@author: Andrew
'''

from pony.orm import Database, Required, Set
from pony.orm.core import db_session

db = Database('sqlite', ':memory:')

class Account(db.Entity):
    name = Required(str)
    addresses = Set("Address")
    
    def say_hi(self):
        print("Hi!  My name is " + self.name)
    
class Address(db.Entity):
    address = Required(str)
    person = Required(Account)
    
@db_session
def get_person(name):
    return Account(name=name)

if __name__ == '__main__':
    db.generate_mapping(create_tables=True)
    p = get_person("Andrew")
    p.say_hi()
    
    
