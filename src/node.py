
class Node:
    def __init__(self, key, tag=0, weight=0.0, info=None, pos=None):
        self.key = key
        self.tag = tag
        self.weight = weight
        self.info = info
        self.pos = pos

    def __str__(self):
        return f"str : Node id # {self.key}"

    def __repr__(self):
        return f"Node id #{self.key}"
