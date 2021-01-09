class Node:
    def __init__(self, id, tag=0, weight=0.0, info=None, pos=None):
        self.id = id
        self.tag = tag
        self.weight = weight
        self.info = info
        if isinstance(pos, str):
            self.pos = eval(pos)
        else:
            self.pos = pos

    def __str__(self):
        return f"str : Node id # {self.id}"

    def __repr__(self):
        return f"Node id #{self.id}"

    def __lt__(self, other):
        return self.weight < other.weight
