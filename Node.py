

class Node:

    def __init__(self, pos):
        self.pos = pos

        self.gValue = 0
        self.fValue = 0
        self.cameFrom = None
        self.num = 0

    @property
    def x(self):
        return self.pos[1]

    @x.setter
    def x(self, value):
        self.pos[0] = value

    @property
    def y(self):
        return self.pos[0]
    @y.setter
    def y(self, value):
        self.pos[1] = value