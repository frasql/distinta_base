from pprint import pprint


""" Different containers for store different items """


class Content:
    def __init__(self, _id, description):
        self.description = description
        self.id = _id

    def __str__(self):
        return "<'{}', '{}'>".format(self.id, self.description)

    def __repr__(self):
        return "Content('{}', '{}')".format(self.id, self.description)

    def __eq__(self, other):
        return isinstance(other, Content) and other.id == self.id

class Container():
    def __init__(self):
        self.data = []

    def insert_content(self, content):
        if isinstance(content, Content):
            for e in self.data:
                if content.id == e.id:
                    raise ValueError(f'Content with id={content.id} already exists in this Container')
            self.data.append(content)
        else:
            raise ValueError('Object must be Content')

    def __str__(self):
        return f"< Container={self.data} >".format(self.data)

    def __repr__(self):
        return f"< Container={self.data} >".format(self.data)

"""
c = Content(1, 'DESCR')
b = Content(1, 'DESCR')

cont1 = Container()
cont2 = Container()

cont1.insert_content(c)
cont2.insert_content(b)
cont2.insert_content(c)

print(cont2)
"""

class Articolo(object):
    def __init__(self, _id, descr, quantita):
        self._id = _id
        self.descr = descr
        self.quantita = quantita
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self):
        self._id = id

    def __str__(self):
        return f"< {self.id}, '{self.descr}', {self.quantita} >"

    def __repr__(self):
        return f"Articolo({self.id}, '{self.descr}', {self.quantita})"


class Level(Articolo):
    def __init__(self, _id, id_artico, descr, quantita):
        Articolo.__init__(self, _id, descr, quantita)
        self.id_artico = id_artico
        self.descr = descr
        self.quantita = quantita
        self.livello = {}

    def __str__(self):
        return f"< {self._id}, {self.id_artico}, '{self.descr}', {self.quantita} >"

    def __repr__(self):
        return f"Level({self._id}, {self.id_artico}, '{self.descr}', {self.quantita})"

a = Articolo(1, 'NEW', 5)

l = Level(a.id, 44, 'Test', 8)

pprint(a)
pprint(l)
