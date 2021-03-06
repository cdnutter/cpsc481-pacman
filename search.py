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

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def baseSearchFunction(problem, data_structure):
    """
    Since the implementation of a Depth First Search and Breadth First Search
    are nearly identical, we can simply switch the date structure based on the
    order we recieve our nodes; i.e. change the direction we pop, push nodes.
    """
    # The path that takes us from the start node to the destination
    answer_path = []

    # Set the open_nodes data structure as either a Stack (DFS) or Queue (BFS)
    open_nodes = data_structure()

    # Add the starting state and the empty list to our open nodes
    open_nodes.push((problem.getStartState(), answer_path))

    # Initialize closed nodes to contain nothing
    closed_nodes = []

    # While there is at least one item in our open_nodes
    while (not open_nodes.isEmpty()):

        # Assign current_node and answer_path to an element from one side of the list
        current_node, answer_path = open_nodes.pop()

        # If our current node isn't closed
        if (current_node not in closed_nodes):

            # Add the current node to the set of closed nodes
            closed_nodes.append(current_node)

            # If we're at the destination
            if (problem.isGoalState(current_node)):
                # Return the path we used to get here
                return answer_path

            # Set successors equal to the children of the current node
            successors = problem.getSuccessors(current_node)

            # For each successor
            for state in successors:

                # Set the node, path equal to the node and path of the state (We're not concerned about the cost)
                node, path, _ = state

                # If the current node isn't in the set of closed nodes
                if (node not in closed_nodes):
                    # Add the node and path to the set of open nodes
                    open_nodes.push((node, answer_path + [path]))

    # Return the 'best' answer_path we could find; If we're returning here, we didn't find the destination
    return answer_path


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""

    # Use a stack in order to perform a Depth First Search
    return baseSearchFunction(problem, util.Stack)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # Use a Queue in order to perform a Breadth First Search
    return baseSearchFunction(problem, util.Queue)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Nodes are looking at and have looked at
    openStates = util.PriorityQueue()
    closedStates = []

    # The state we are currently looking at
    initialize = [problem.getStartState(), [], 0]
    startState = problem.getStartState()
    openStates.push(initialize, 0)

    while(not openStates.isEmpty()):
        # find node with least cost, this is next step
        # remove nextstep from openstates
        # nextStep = openStates.pop()
        node, actions, currentCost = openStates.pop()

        if node in closedStates:
            continue

        closedStates.append(node)

        # if the goal state has been reached then return the path that it took to get there
        if problem.isGoalState(node):
            return actions

        # Generate successors
        # For each successor add its path to the dictionary final path and push it into the priority queue
        for successor in problem.getSuccessors(node):
            state, _actions, cost = successor
            fn = cost + currentCost
            openStates.push((state, actions + [_actions], fn), fn + heuristic(state, problem))

    return actions

def cost_of(state, problem, heuristic=nullHeuristic):
    cost = state[2] + heuristic(state[0], problem)
    return cost

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

