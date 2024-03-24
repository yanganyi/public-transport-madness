class Entity:
    def __init__(self,name,id):
        self.name=name; self.id=id

    def __str__(self):
        return "Entity(name=%s id=%d)" % (self.name,self.id)

class Bus(Entity):
    def __init__(self,name,id):
        super().__init__(name,id)

class Train(Entity):
    def __init__(self,name,id):
        super().__init__(name,id)
        # Create a list of buses and trains
        b1 = Bus("B1", 0); t23456789_1 = Train('T2', 't')
        
                                               

class DoubleDecker(Bus):
    pass

class BusStop(Entity):
    pass

class Interchange(BusStop):
    pass

class Person(Entity):
    pass