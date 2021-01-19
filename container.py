""" Same container for store different items """


class Commessa(object):
    commesse = []

    def __init__(self, _id, description):
        self.description = description
        self._index = -1

        if _id in self.commesse:
            raise ValueError(f'Commessa with id={_id} already exists')
        else:
            self._id = _id
            self.commesse.append(_id)

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"{self.id}, {self.description}"

    def __repr__(self):
        return f"Commessa({self.id}, '{self.description}')"


class Container(object):
    projects = []
    
    @classmethod
    def insert_project(cls, commessa):
        if isinstance(commessa, Commessa):
            cls.projects.append(commessa)
        else:
            raise ValueError('Only Commessa objects are allowed')

    def __str__(self):
        return f"Container({self.projects})"

    def __repr__(self):
        return f"Container({self.projects})"

    
c = Commessa(1, 'new')
p = Commessa(2, 'other')


Container.insert_project(c)
Container.insert_project(p)


print(Container.projects)