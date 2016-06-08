import pickle
import uuid

class DB:
    __filename__ = 'db.pickle'
    __loaded__ = False
    __dirty__ = False
    registry = {}
    translations = {}
    
    def add(self, model)
        self.dirty = True
        self.registry[model.id] = model

    def remove(self, _id):
        del self.registry[_id]
        
    def save(self):
        pickle.dump("db.pickle", self.registry)

    def __repr__(self):
        return str(self.registry)
        
    def find(self, _id):
        try:
            return self.registry[_id]
        except KeyError:
            return None

class Model:
    def __init__(self, _id=None, **kwargs):
        if _id is None:
            self.id = uuid.uuid4().int
        else:
            self.id == _id
        for key, value in **kwargs:
            setattr(self, key, value)
        
def init():
    db = DB()
    home = Model(url='', filename='index.html', lang='en', source="home.j2")
    db.add(home)
    db.add(home
    
