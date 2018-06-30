

class Node:

    def __init__(self, pos):
        self.pos = pos

        self.gValue = 1000000
        self.fValue = 0
        self.cameFrom = None
        self.num = 0

        self.inOpen = False
        self.inClosed = False

        self.isStart = False
        self.isGoal = False
        self.isWall = False
        self.isSolution = False

        self.neighbors = []

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self, value):
        self.pos[0] = value

    @property
    def y(self):
        return self.pos[1]

    @y.setter
    def y(self, value):
        self.pos[1] = value

    @property
    def color(self):
        if self.isStart:
            return 82, 239, 43
        elif self.isGoal:
            return 239, 52, 42
        elif self.isWall:
            return 0, 0, 0
        elif self.isSolution:
            return 82, 239, 43
        else:
            if self.inOpen:
                return 91, 227, 255
            else:
                return 247, 240, 239

    @property
    def width(self):
        if self.isStart or self.isGoal or self.isWall or self.inClosed or self.inOpen or self.isSolution:
            return 0
        else:
            return 2
