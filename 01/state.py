# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:37:52 2019

@author: HERAMB

state  - Location of all the tiles, including blank one
parent - parent of the current state
move   - from which move did we obtain the current state
depth  - depth of current state
cost   - cost of current state
key    - decided by the heuristic function


"""

class State:

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map