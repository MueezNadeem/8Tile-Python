# Assignment by:  20L-0947 & 20L-0928

from os import system

import copy

GoalState = ['1', '2', '3', '4', '5', '6', '7', '8', 'X']


class Tiles:  # Class to define the Puzzle Layout
    config = []  # Array to contain the layout of Puzzle
    empty_coordinates = 0  # Index of empty space

    def __init__(self, c):
        self.config = c
        self.empty_coordinates = c.index('X')

    def print_tiles(self):  # Function to print the tiles of the puzzle
        for i in range(0, len(self.config), 1):
            if ((i+1) % 3 == 0):
                print(self.config[i])
            else:
                print(self.config[i], end=" ")


def moveUp(x: Tiles):  # Function to move up the empty space
    if x.empty_coordinates >= 0 and x.empty_coordinates <= 2:  # Check if empty space is in 1st row
        return False
    else:
        temp = copy.deepcopy(x)
        temp.config[temp.empty_coordinates], temp.config[temp.empty_coordinates -
                                                         3] = temp.config[temp.empty_coordinates-3], temp.config[temp.empty_coordinates]
        temp.empty_coordinates = temp.empty_coordinates-3
        return temp


def moveDown(x: Tiles):  # Function to move down the empty space
    if x.empty_coordinates >= 6 and x.empty_coordinates <= 8:  # Check if empty space is in 3rd row
        return False
    else:
        temp = copy.deepcopy(x)
        temp.config[temp.empty_coordinates], temp.config[temp.empty_coordinates +
                                                         3] = temp.config[temp.empty_coordinates+3], temp.config[temp.empty_coordinates]
        temp.empty_coordinates = temp.empty_coordinates+3
        return temp


def moveLeft(x: Tiles):  # Function to move left the empty space
    if x.empty_coordinates % 3 == 0:  # Check if empty space is in 1st column
        return False
    else:
        temp = copy.deepcopy(x)
        temp.config[temp.empty_coordinates], temp.config[temp.empty_coordinates -
                                                         1] = temp.config[temp.empty_coordinates-1], temp.config[temp.empty_coordinates]
        temp.empty_coordinates = temp.empty_coordinates-1
        return temp


def moveRight(x: Tiles):  # Function to move right the empty space
    if (x.empty_coordinates-2) % 3 == 0:  # Check if empty space is in 3rd column
        return False
    else:
        temp = copy.deepcopy(x)
        temp.config[temp.empty_coordinates], temp.config[temp.empty_coordinates +
                                                         1] = temp.config[temp.empty_coordinates+1], temp.config[temp.empty_coordinates]
        temp.empty_coordinates = temp.empty_coordinates+1
        return temp


def check(visited, temp):  # Function to check if the an instance of Tiles object has been already visited
    check = False
    for x in visited:
        if (x.config == temp.config):
          return True
    return check


def bfs(x: Tiles):  # Function for Breadth First Search (BFS) traversal
    graph = {}
    visited = []
    queue = []  # fifo

    queue.append(x)
    while len(queue) > 0:
        print('\t\t------New Iteration---------')
        temp = queue.pop(0)
        visited.append(temp)
        graph[temp] = []
        print('Current Layout of Tiles : ')
        temp.print_tiles()

        a = moveUp(temp)
        # move up only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nUP SHIFT')
            a.print_tiles()
#        print(graph)

        a = moveDown(temp)
        # move down only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nDown SHIFT')
            a.print_tiles()
       # print(graph)

        a = moveLeft(temp)
        # move left only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nLeft SHIFT')
            a.print_tiles()
        # print(graph)

        a = moveRight(temp)
        # move right only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nRight SHIFT')
            a.print_tiles()
    #    print(graph)

        for x in graph[temp]:  # Add the child nodes of current Tiles Object to the queue
            queue.append(x)
        # for x in queue:
        #     print('-----')
        #     x.print_tiles()

        for x in queue:  # Check if Queue contains the Goal State
            if (x.config == GoalState):
                print('Found')
                return


def dfs(x: Tiles, _visited, _graph):  # Function for Depth First Search (DFS)
    if (_graph == None):  # If graph does not exist, create new graph otherwise assign the previous graph
        graph = {}
    else:
        graph = _graph

    if (_visited == None):  # If visited list does not exist, create new visited list otherwise assign the previous visited list
        visited = []
    else:
        visited = _visited

    stack = []
    stack.append(x)

    print('\t\t------New Iteration---------')
    temp = stack.pop(len(stack)-1)
    visited.append(temp)
    graph[temp] = []
    print('Current Layout of Tiles : ')
    temp.print_tiles()

    a = moveUp(temp)
    # move up only if allowed and resultant configuration is not visited
    if (a != False and check(visited, a) == False):
        graph[temp].append(a)
        print('\nUP SHIFT')
        a.print_tiles()
        if a.config == GoalState:  # if current layout of tiles is same as Goal State, return
            print('Found')
            return True
        if dfs(a, visited, graph) == True:  # traverse the graph in DFS manner
            return True

#        print(graph)

    a = moveDown(temp)

    # move down only if allowed and resultant configuration is not visited
    if (a != False and check(visited, a) == False):
        graph[temp].append(a)
        print('\nDown SHIFT')
        a.print_tiles()
        if a.config == GoalState:  # if current layout of tiles is same as Goal State, return
            print('Found')
            return True
        if dfs(a, visited, graph) == True:  # traverse the graph in DFS manner
            return True

    # print(graph)

    a = moveLeft(temp)

    # move left only if allowed and resultant configuration is not visited
    if (a != False and check(visited, a) == False):
        graph[temp].append(a)
        print('\nLeft SHIFT')
        if a.config == GoalState:  # if current layout of tiles is same as Goal State, return
            print('Found')
            return True
        a.print_tiles()
        if dfs(a, visited, graph) == True:  # traverse the graph in DFS manner
            return True

        # print(graph)

    a = moveRight(temp)

    # move right only if allowed and resultant configuration is not visited
    if (a != False and check(visited, a) == False):
        graph[temp].append(a)
        print('\nRight SHIFT')
        a.print_tiles()
        if a.config == GoalState:  # if current layout of tiles is same as Goal State, return
            print('Found')
            return True
        if dfs(a, visited, graph) == True:  # traverse the graph in DFS manner
            return True

    return False  # if above conditions are not met, return false


def ids(x: Tiles, _lvl, _visited):  # Function for Iterative Deepening Search (IDS)
    graph = {}
    queue = []
    if _visited == None:  # If visited list does not exist, create new visited list otherwise assign the previous visited list
        visited = []
    else:
        visited = _visited
    totalnodes = 0  # Total number of nodes at current level
    for i in range(0, _lvl, 1):
        totalnodes = totalnodes+pow(4, i)
    queue.append(x)
    print('\nCurrent Level Limit: '+str(_lvl))

    for i in range(0, totalnodes, 1):  # lvl start from zero

        temp = queue.pop(0)
        print('--------- Parent Config-------')
        temp.print_tiles()
        visited.append(temp)
        graph[temp] = []

        a = moveUp(temp)
       # i=i+1
        # move up only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nUp SHIFT')
            queue.append(a)
            a.print_tiles()
            if a.config == GoalState:  # If current configuration meets the goal state
                print('Found')
                return True

        a = moveDown(temp)
       # i=i+1
        # move down only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nDown SHIFT')
            queue.append(a)
            a.print_tiles()
            if a.config == GoalState:  # If current configuration meets the goal state
                print('Found')
                return True

        a = moveLeft(temp)
       # i=i+1
        # move left only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nLeft SHIFT')
            queue.append(a)
            a.print_tiles()
            if a.config == GoalState:  # If current configuration meets the goal state
                print('Found')
                return True

        a = moveRight(temp)
       # i=i+1
        # move right only if allowed and resultant configuration is not visited
        if (a != False and check(visited, a) == False):
            graph[temp].append(a)
            print('\nRight SHIFT')
            queue.append(a)
            a.print_tiles()
            if a.config == GoalState:  # If current configuration meets the goal state
                print('Found')
                return True

    if ids(x, _lvl+1, visited) == True:  # Check if Goal State is found in next levels
        return True

    return


# Configuration of tiles for Tiles Object (Initial State)
arr = ['1', '2', '3', '4', 'X', '6', '7', '5', '8']

x = Tiles(arr)
print('--------------IDS--------------')
ids(x, 0, None)
input()
system('cls')


print('--------------DFS--------------')
dfs(x, None, None)
input()
system('cls')

print('--------------BFS--------------')
bfs(x)
