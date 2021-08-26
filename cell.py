class Cell:
    def __init__(self, alive):
        self.alive = alive
        self.alive = False

    # Change status
    def setDead(self):
        self.alive = False
        return self.alive

    def setAlive(self):
        self.alive = True
        return self.alive

    # Get status
    def isAlive(self):
        if self.alive:
            return True
        return False

    def getStatusSign(self):
        if self.alive:
            return 'O'
        return '.'
