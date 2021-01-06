
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

    def __lt__(self, other):
        if self.weight == other.weight:
            return 0
        elif self.weight > other.weight:
            return 1
        else:
            return -1

