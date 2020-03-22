
class Vertex: 
    def __init__(self, key: int):
        self.id: int = key
        self.connected_to: dict = {}
    
    def add_neighbour(self, nbr: Vertex, weight: int=0):
        self.connected_to[nbr]: int = weight 

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connected_to])
    
    def get_connections(self):
        pass