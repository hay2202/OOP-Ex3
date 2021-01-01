
class Node:
    def __init__(self, key,pos):
        self.id = key
        self.tag = 0
        self.weight = 0.0
        self.info = None
        self.pos = pos

    def __str__(self):
        return f"str : Node id # {self.id}"

    def __repr__(self):
        return f"Node id #{self.id}"
