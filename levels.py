from pprint import pprint

""" Codice Livello1 contenente lista di codici Livello2 """
class Livello1(object):
    def __init__(self, id, codice, descrizione, quantita, liv2=[]):
        self._id = id
        self.codice = codice
        self.descrizione = descrizione
        self.quantita = quantita
        self.liv2 = []
        self._index = -1
    
    @property
    def id(self):
        return self._id

    def add_liv2(self, level):
        if isinstance(level, Livello2):
            for e in self.liv2:
                if level.id == e.id:
                    raise ValueError("Livello2 with id={} already exists in this Livello1".format(level.id))
            self.liv2.append(level)
        else:
            raise ValueError('Object must be Livello2')

    def __str__(self):
        return "< {}, '{}', '{}', {}, {} >".format(self.id, self.codice, self.descrizione, self.quantita, self.liv2)

    def __repr__(self):
        return "Livello1({}, '{}', '{}', {}, {})".format(self.id, self.codice, self.descrizione, self.quantita, self.liv2)
    
    def __eq__(self, other):
        return isinstance(other, Livello1) and other.id == self.id 


""" Codice Livello2 contenente lista di codici Livello3 """
class Livello2(object):
    def __init__(self, id, codice, descrizione, quantita, liv3=[]):
        self._id = id
        self.codice = codice
        self.descrizione = descrizione
        self.quantita = quantita
        self.liv3 = []
    
    @property
    def id(self):
        return self._id

    def add_liv3(self, level):
        if isinstance(level, Livello3):
            for e in self.liv3:
                if level.id == e.id:
                    raise ValueError(f'Content with id={level.id} already exists in this Livello3')
            self.liv3.append(level)
        else:
            raise ValueError('Object must be Livello3')

    def __str__(self):
        return "< {}, '{}', '{}', {}, {} >".format(self.id, self.codice, self.descrizione, self.quantita, self.liv3)

    def __repr__(self):
        return "Livello2({}, '{}', '{}', {}, {})".format(self.id, self.codice, self.descrizione, self.quantita, self.liv3)
    
    def __eq__(self, other):
        return isinstance(other, Livello2) and other.id == self.id 


""" Codice Livello3 contenente lista di codici Livello4 """
class Livello3(object):
    def __init__(self, id, codice, descrizione, quantita, liv4=[]):
        self._id = id
        self.codice = codice
        self.descrizione = descrizione
        self.quantita = quantita
        self.liv4 = []

    @property
    def id(self):
        return self._id
    
    def add_liv4(self, level):
        if isinstance(level, Livello4):
            for e in self.liv4:
                if level.id == e.id:
                    raise ValueError(f'Content with id={level.id} already exists in this Livello4')
            self.liv4.append(level)
        else:
            raise ValueError('Object must be Livello4')

    def __str__(self):
        return "< {}, '{}', '{}', {}, {} >".format(self.id, self.codice, self.descrizione, self.quantita, self.liv4)

    def __repr__(self):
        return "Livello3({}, '{}', '{}', {}, {})".format(self.id, self.codice, self.descrizione, self.quantita, self.liv4)

    def __eq__(self, other):
        return isinstance(other, Livello3) and other.id == self.id 


class Livello4(object):
    def __init__(self, id, codice, descrizione, quantita, liv5=[]):
        pass


""" Commessa contenente codici primari """
class Commessa(object):
    commesse = []

    def __init__(self, numero, descrizione, cliente):
        
        self.descrizione = descrizione
        self.cliente = cliente
        self.liv1 = []

        if numero in self.commesse:
            raise ValueError(f'Commessa with id={numero} already exists')
        else:
            self._numero = numero
            self.commesse.append(numero)

    @property
    def numero(self):
        return self._numero
        
    def insert_level(self, level):
        if isinstance(level, Livello1):
            for e in self.liv1:
                if level.id == e.id:
                    raise ValueError(f'Livello1 with id={level.id} already exists in this Commessa')
            self.liv1.append(level)
        else:
            raise ValueError('Object must be Livello1')
    
    def __str__(self):
        return "< {}, '{}', '{}', {} >".format(self.numero, self.descrizione, self.cliente, self.liv1)

    def __repr__(self):
        return "Commessa({}, '{}', '{}', {})".format(self.numero, self.descrizione, self.cliente, self.liv1)


artico1 = Livello1(13, 'AZFG', 'Ruota', 3)
artico2 = Livello1(10, 'AFND', 'ROL', 5)
artico3 = Livello2(5, 'DLSK', 'Line', 7)
artico4 = Livello2(3, 'DIJR', 'test', 4)

artico5 = Livello3(6, 'LFL', 'new_descr', 5)

try:
    artico1.add_liv2(artico3)
    artico1.add_liv2(artico4)
    artico3.add_liv3(artico5)
except ValueError as err:
    print(err)

c1 = Commessa(1, 'HHHH', 'DESCR')
c2 = Commessa(2, 'FHFJKD', 'Other DESC')

try:
    c1.insert_level(artico1)
    c2.insert_level(artico1)
    c1.insert_level(artico2)
except ValueError as err:
    print(err)


try:
    pprint(c1)
    pprint(c2)
except ValueError as err:
    pprint(err)

