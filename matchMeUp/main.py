'''
Created on Jun 27, 2015

@author: Andrew
'''
from matchMeUp import app, db
from matchMeUp.models.orm import define_entities

if __name__ == '__main__':
    define_entities(db)
    app.run(debug=True)
