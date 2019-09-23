# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:03:51 2019

@author: HERAMB

24 puzzle problem

Initial State
--------------------------
| 9  | 24 |	3  | 5  | 17 |
--------------------------
| 6	 |    | 13 | 19 | 10 |
--------------------------
| 11 | 21 |	12 | 1  | 20 |
--------------------------
| 16 | 4  | 14 | 12 | 15 |
--------------------------
| 8  | 18 |	23 | 2  |  7 |
--------------------------

---- 0 is a blank tile which can be moved


Goal State
--------------------------
| 1  | 2  | 3  | 4  | 5  | 
--------------------------
| 6  | 7  | 8  | 9  | 10 | 
--------------------------
| 11 | 12 | 13 | 14 | 15 | 
--------------------------
| 16 | 17 | 18 | 19 | 20 | 
--------------------------
| 21 | 22 | 23 | 24 |  0 | 
--------------------------

"""
#import libraries
from math import sqrt
from collections import deque
from state import State
from heapq import heappush, heappop, heapify
import time


#--- Specify a goal state which will be tested to stop the program.
goalState = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,0]
goalNode = State
initialState = []   #--- Initial State to be empty List
puzzleLen = 0       #--- Length of the puzzle (Eg - for 24 puzzle problem, len = 25)  
puzzleSide = 0      #--- Length of puzzleSide (Eg - for 24 puzzle problem, side = 5)

nodesExpanded = 0   #--- no of nodes expanded, will be used in the end, initial = 0
maxDepthReached = 0 #--- Length of the depth reached
maxFringeSize = 0   #--- Maximum Size of Fringe, will be used in the end, initial = 0

moves = []          #--- this keeps track of all the moves that are required to reach the goal state


"""
Function - bfs() (Breadth First Search)
    - works as a Breadth First Search algorithm.
"""
def bfs(startState):

    global goalNode, maxFringeSize, maxDepthReached
    
    visited, queue = set(), deque([State(startState, None, None, 0, 0, 0)])
    while queue:                            #--- Execute until we have elements left in queue 
        node = queue.popleft()              #--- pop the first state
        
        visited.add(node.map)               #--- Keep Track of Visited Nodes
        
        #--- Goal Test
        if node.state == goalState:
            goalNode = node
            return True, queue
        
        #--- If not a goal state then expand the node
        childNodes = expand(node)
        
        for child in childNodes:            #--- Traverse every child in the Level
            if child.map not in visited:    #--- Check if visited or not
                queue.append(child)         #--- if not visited append as a child
                visited.add(child.map)      #--- add it to the visited nodes set
                
                if child.depth > maxDepthReached:
                    maxDepthReached += 1
        
        if len(queue) > maxFringeSize:
            maxFringeSize = len(queue)
    
    #--- if search is complete and goal state not reached then return goal not found
    return False, None       
    
"""
Function - dfs() (Breadth First Search)
    - works as a Depth First Search algorithm.

"""
def dfs(startState):
    
    global goalNode, maxFringeSize, maxDepthReached
    
    visited, stack = set(), list([State(startState, None, None, 0, 0, 0)])

    while stack:                                #--- Execute until we have elements left in queue

        node = stack.pop()                      #--- pop the first state

        visited.add(node.map)                   #--- Keep Track of Visited Nodes

        if node.state == goalState:
            goalNode = node
            return True, stack

        neighbors = reversed(expand(node))

        for neighbor in neighbors:              #--- Traverse every child in the depth
            if neighbor.map not in visited:     #--- Check if visited or not
                stack.append(neighbor)          #--- if not visited append as a child
                visited.add(neighbor.map)       #--- add it to the visited nodes set

                if neighbor.depth > maxDepthReached:
                    maxDepthReached += 1

        if len(stack) > maxFringeSize:
            maxFringeSize = len(stack)
    
    #--- if search is complete and goal state not reached then return goal not found
    return False, None

"""
Function - greedy() (Greedy Search)
    - works as a Greedy Search with using a heuristic function.

"""
def greedy(startState):
    
    global goalNode, maxFringeSize, maxDepthReached
    #--- get the heuristic function first
    heuristic = input('-- Please select the Heuristic Function\
                      \n h1 : number of misplaced tiles\
                      \n h2 : sum of the distances of every tile to its goal position.\
                      \n-- Enter your choice : ')
    heuristicFunc = heuristic_map[heuristic]
    visited, pQueue = set(), list()
    key = heuristicFunc(startState)
    root = State(startState, None, None, 0, 0, key)
    entry = (key, 0, root)
    heappush(pQueue, entry)
    while pQueue:

        node = heappop(pQueue)
        #print(node)
        visited.add(node[2].map)

        if node[2].state == goalState:
            goalNode = node[2]
            return True, pQueue

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = heuristicFunc(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in visited:

                heappush(pQueue, entry)

                visited.add(neighbor.map)

                if neighbor.depth > maxDepthReached:
                    maxDepthReached += 1
                    
        if len(pQueue) > maxFringeSize:
            maxFringeSize = len(pQueue)
    #--- if search is complete and goal state not reached then return goal not found
    return False, None


"""
Function - ast() (A star Search)
    - works as a A star Search algorithm.

"""
def ast(startState):
    
    global goalNode, maxFringeSize, maxDepthReached
    #--- get the heuristic function first
    heuristic = input('-- Please select the Heuristic Function\
                      \n h1 : number of misplaced tiles\
                      \n h2 : sum of the distances of every tile to its goal position.\
                      \n-- Enter your choice : ')
    heuristicFunc = heuristic_map[heuristic]
    visited, pQueue = set(), list()
    key = heuristicFunc(startState)
    root = State(startState, None, None, 0, 0, key)
    entry = (key, 0, root)
    heappush(pQueue, entry)
    while pQueue:

        node = heappop(pQueue)
        #print(node)
        visited.add(node[2].map)

        if node[2].state == goalState:
            goalNode = node[2]
            return True, pQueue

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + heuristicFunc(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in visited:

                heappush(pQueue, entry)

                visited.add(neighbor.map)

                if neighbor.depth > maxDepthReached:
                    maxDepthReached += 1
                    
        if len(pQueue) > maxFringeSize:
            maxFringeSize = len(pQueue)
    #--- if search is complete and goal state not reached then return goal not found
    return False, None

"""
Function - h1() (Heuristic Function 1 : number of misplaced tiles)
    - works as a A star Search algorithm.

"""
def h1(state):
    count = 0
    for i in range(0,puzzleLen):
        if not (state.index(i) == goalState.index(i)) : 
            count+=1
    return count 
"""
Function - h2() (Heuristic Function 2 : sum of the distances of every tile to its goal position.)
    - works as a A star Search algorithm.

"""

def h2(state): 
    return sum(abs(p%puzzleSide - g%puzzleSide) + abs(p//puzzleSide - g//puzzleSide)
               for p,g in ((state.index(i),goalState.index(i)) 
               for i in range(1, puzzleLen))) 

   
"""
Function - expand()
    - expands the node and creates valid child nodes
    - returns all valid child nodes of the current node 
"""
def expand(node):
    global nodesExpanded
    nodesExpanded += 1
    childNodes = []
    
    #Append all the child to childNode for a valid move
    childNodes.append(State(validMove(node.state,'D'),node,'D',node.depth + 1, node.cost + 1, 0)) #--- Down
    childNodes.append(State(validMove(node.state,'L'),node,'L',node.depth + 1, node.cost + 1, 0)) #--- Left
    childNodes.append(State(validMove(node.state,'R'),node,'R',node.depth + 1, node.cost + 1, 0)) #--- Right
    childNodes.append(State(validMove(node.state,'U'),node,'U',node.depth + 1, node.cost + 1, 0)) #--- UP
    
    nodes = [child for child in childNodes if child.state]
    return nodes

"""
Function validMove()
    - validates the next move as valid or invalid
    - returns valid state if move is valid otherwise returns None
"""
def validMove(state, position):
    newState = state[:]
    index = newState.index(0) #--- get the position of blank tile
    if position == 'U':  # Up

        if index not in range(0, puzzleSide): #--- Valid iff not present in top row
            #--- Swap the empty tile with top element
            temp = newState[index - puzzleSide]
            newState[index - puzzleSide] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'D':  # Down
        #--- Swap the empty tile with bottom element
        if index not in range(puzzleLen - puzzleSide, puzzleLen):

            temp = newState[index + puzzleSide]
            newState[index + puzzleSide] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'L':  # Left

        if index not in range(0, puzzleLen, puzzleSide):

            temp = newState[index - 1]
            newState[index - 1] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None

    if position == 'R':  # Right

        if index not in range(puzzleSide - 1, puzzleLen, puzzleSide):

            temp = newState[index + 1]
            newState[index + 1] = newState[index]
            newState[index] = temp

            return newState
        else:
            return None
"""
Function - get(dataList) 
    - Reads input from user and updates puzzle configuration
"""
def get(dataList):
    global puzzleLen, puzzleSide
    
    data = dataList.split(',') 
    for element in data:
        initialState.append(int(element))
    puzzleLen = len(initialState)                   #--- get the length f puzzle
    puzzleSide = int(sqrt(puzzleLen))       #--- calculate square root in order to get the length of puzzle size

"""
Function - backtrack()
"""
def backtrack():
    currentNode = goalNode
    while initialState != currentNode.state : #--- terminating condition when we reach top node from bottom 
        moves.insert(0, currentNode.move)
        currentNode = currentNode.parent
    return moves

"""
Function - output(fringe, time)
    - creates an output file with all the required elements
"""
def output(fringe, time):
    if fringe:
        
        global moves
        
        moves = backtrack() #--- get all the moves performed to reach the goal state
        file = open('testcase_bfs.txt', 'w')
        file.write("\npath_to_goal: " + str(moves))
        file.write("\ncost_of_path: " + str(len(moves)))
        file.write("\nnodes_expanded: " + str(nodesExpanded))
        file.write("\nfringe_size: " + str(len(fringe)))
        file.write("\nmax_fringe_size: " + str(maxFringeSize))
        file.write("\nsearch_depth: " + str(goalNode.depth))
        file.write("\nmax_search_depth: " + str(maxDepthReached))
        file.write("\nrunning_time: " + format(time, '.8f'))
        file.close()
    else :
        file = open('testcase_unsolvable.txt', 'w')
        file.write("<-- # UNSOLVABLE # -->")
        file.write("\nnodes_expanded: " + str(nodesExpanded))
        file.write("\nmax_fringe_size: " + str(maxFringeSize))
        file.write("\nmax_search_depth: " + str(maxDepthReached))
        file.write("\nrunning_time: " + format(time, '.8f'))
        file.close()

"""
Function - main() 
    - Executed everytime the python file starts.
"""
def main():
    algorithm = input('--> Please select the algorithm \
                      \n1. bfs : Breadth First Search \
                      \n2. dfs : Depth First Search \
                      \n3. ast : A Star Search\
                      \n4. greedy : Greedy Search\
                      \n enter the selection : ')
    
    data = input('--> Enter puzzle elements : ')
    
    get(data)
    
    function = function_map[algorithm]
    
    start = time.time()

    search, fringe = function(initialState)

    stop = time.time()
    
    if search : 
        output(fringe, stop-start)
    else : 
        print('Validated all the possible states but goal state not found')
        print('<-- # UNSOLVABLE # -->')
        output(fringe, stop-start)

function_map = {
    'bfs': bfs,
    'dfs': dfs,
    'greedy' : greedy,
    'ast' : ast
    }

heuristic_map = {
        'h1' : h1,
        'h2' : h2
        }

if __name__ == '__main__':
    main()