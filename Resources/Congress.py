from .Conferee import Conferee
from .Connection import Connection
from random import *


class Congress:

    def __init__(self):
        self.root = None
        self.max = 0
        self.parties = []
        self.connections = []

    def add(self, parent, party, id, name):
        newconferee = Conferee(party, id, name)
        if self.root is None:
            self.root = newconferee
        else:
            self.max += 1
            newconferee.id = self.max
            self.root = self.addNode(self.root, parent, newconferee)
            self.set_position(self.root, 0, None, 0)

    def addNode(self, actual, parent, conferee):
        if actual is None:
            return actual
        if actual == parent:
            if actual.left is None:
                actual.left = conferee
                self.addConnection(actual, actual.left)
            elif actual.center is None:
                actual.center = conferee
                self.addConnection(actual, actual.center)
            elif actual.right is None:
                actual.right = conferee
                self.addConnection(actual, actual.right)
            else:
                actual.outside = True
            return actual
        actual.left = self.addNode(actual.left, parent, conferee)
        actual.center = self.addNode(actual.center, parent, conferee)
        actual.right = self.addNode(actual.right, parent, conferee)
        return actual

    def deleteNode(self, conferee, id):
        if conferee.left is not None and conferee.right is not None or conferee.center is not None:
            conferee = conferee.left
            if conferee.left.left is not None or conferee.left.center is not None or conferee.left.right is not None:
                conferee.right.left = conferee.left.left
                conferee.right.center = conferee.left.center
                conferee.right.right = conferee.left.right
        elif conferee.left is not None and conferee.right.left is None and conferee.right.center is None and conferee.right.right is None:
            conferee = conferee.left
            if conferee.left.left is not None or conferee.left.center is not None or conferee.left.right is not None:
                conferee.left = conferee.left.left
                conferee.center = conferee.left.center
                conferee.right = conferee.left.right

    def addConnection(self, c1, c2):
        conect = Connection(c1, c2)
        conAux = Connection(c2, c1)
        if conect in self.connections or conAux in self.connections:
            return
        self.connections.append(conect)
        c1.adjacent.append(c2)
        c2.adjacent.append(c1)

    def set_position(self, current, i, previous, j):
        if current is not None:
            if i == 0:
                current.x = 660
                current.y = 10
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            elif i == 1:
                current.x = previous.x - (320 - j)
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            elif i == 2:
                current.x = previous.x
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            else:
                current.x = previous.x + (320 - j)
                current.y = previous.y + 100
                current.rect.x = current.x
                current.rect.y = current.y
                previous = current
            self.set_position(current.left, 1, previous, j + 70)
            self.set_position(current.center, 2, previous, j + 70)
            self.set_position(current.right, 3, previous, j + 70)
