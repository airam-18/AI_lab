# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from os import stat_result

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    "*** YOUR CODE HERE ***"
    dfsStack =util.Stack()
    visited = set()

    start_state=problem.getStartState()
    dfsStack.push((start_state,[]))


    while not dfsStack.isEmpty():
        current_state, actions = dfsStack.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state in visited:
            continue

        visited.add(current_state)

        for next_state, action, stepCost in problem.getSuccessors(current_state):
            if next_state not in visited:
                new_actions = actions+[action]
                dfsStack.push((next_state,new_actions))

    return  []

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    bfsQueue = util.Queue()
    visited = set()

    start_state= problem.getStartState()
    bfsQueue.push((start_state,[]))

    while not bfsQueue.isEmpty():
        current_state, actions = bfsQueue.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state in visited:
            continue

        visited.add(current_state)

        for successor, action, stepCost in problem.getSuccessors(current_state):
            if successor not in visited:
                new_actions = actions+[action]
                bfsQueue.push((successor, new_actions))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    ucsQueue= util.PriorityQueue()
    visited = set()

    start_state= problem.getStartState()

    ucsQueue.push((start_state,[],0),0)

    while not ucsQueue.isEmpty():

        current_state, actions, current_cost = ucsQueue.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state  in visited:
            continue
        visited.add(current_state)

        for succesor,  action, stepCost in problem.getSuccessors(current_state):
            if succesor not in visited:
                new_actions = actions+[action]
                new_cost = current_cost+stepCost
                ucsQueue.push((succesor, new_actions, new_cost),new_cost)

    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    astarQueue = util.PriorityQueue()
    visited_costs = {}

    start_state = problem.getStartState()
    start_cost = 0
    start_priority = start_cost + heuristic(start_state, problem)

    astarQueue.push((start_state,[],start_cost),start_priority)

    while not astarQueue.isEmpty():
        current_state, actions, current_cost = astarQueue.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited_costs or current_cost <= visited_costs[current_state]:
            visited_costs[current_state] = current_cost

            for next_state, action, stepCost in problem.getSuccessors(current_state):
                new_cost = current_cost + stepCost

                if next_state not in visited_costs or new_cost < visited_costs[next_state]:
                    visited_costs[next_state] = new_cost
                    new_actions = actions+[action]

                    f_costs = new_cost + heuristic(next_state, problem)
                    astarQueue.push((next_state,new_actions,new_cost),f_costs)


    return []
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
