"""This is where the problem is defined. Initial state, goal state and other information that can be got from the problem"""
import copy
import queue
import sys, time

# board rule
N = 0
rule={9:[3, 3]}

class Problem(object):

    def __init__(self, initial, goal=None):
        """This is the constructor for the Problem class. It specifies the initial state, and possibly a goal state,
         if there is a unique goal.  You can add other arguments if the need arises"""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

    def result(self, state):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

        """Find the first position which is 0 """
        row = -1
        col = -1
        find = False
        for x in range(N):
            if(find == True):
                break
            for y in range(N):
                if(state[x][y] == 0):
                    find = True
                    row = x
                    col = y
                    break
        if(find == False):
            return []
        else:
            result = []
            """establish the number which showed up in this row  and this column """
            b = [True for i in range(N+1)]
            for x in range(N):
                b[state[row][x]] = False
                b[state[x][col]] = False
            """establish the number which showed up in small box"""
            for x in range(rule[N][0]):
                for y in range(rule[N][1]):
                    b[state[row//rule[N][0]*rule[N][0]+x][col//rule[N][1]*rule[N][1]+y]] = False
            for x in range (1,N+1):
                if(b[x] == True):
                    newState = copy.deepcopy(state)
                    newState[row][col] = x
                    node = Node(newState)
                    result.append(node)
            return result

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough.
        This must be written by students"""
        for x in range(N):
            """check one row"""
            b = [False for i in range(N+1)]
            for y in range(N):
                if((b[state[x][y]] == True) or (state[x][y] == 0)):
                    return False
                else:
                    b[state[x][y]] = True
            """check one column"""
            b = [False for i in range(N+1)]
            for y in range(N):
                if(b[state[y][x]] == True or state[y][x] == 0):
                    return False
                else:
                    b[state[y][x]] = True
            """check the small box"""
            b = [False for i in range(N+1)]
            for p in range(rule[N][0]):
                for q in range(rule[N][1]):
                     if(b[state[x//rule[N][0]*rule[N][0]+p][x%rule[N][0]*rule[N][1]+q]] == True or state[x//rule[N][0]*rule[N][0]+p][x%rule[N][0]*rule[N][1]+q] == 0):
                         return False
                     else:
                         b[state[x//rule[N][0]*rule[N][0]+p][x%rule[N][0]*rule[N][1]+q]] = True

        return True

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state"""

    def __init__(self, state, parent=None, action=None):
        """Create a search tree Node, derived from a parent by an action.
        Update the node parameters based on constructor values"""
        # update(self, state=state, parent=parent, action=action, depth=0)
        # If depth is specified then depth of node will be 1 more than the depth of parent
        self.state = state
        if parent:
            self.depth = parent.depth + 1
            self.parent = parent
        else:
            self.depth = 0

    def expand(self, problem):
        # List the nodes reachable in one step from this node.
        return self.child_node(problem)
    def child_node(self, problem):
        next = problem.result(self.state)
        return next


global NotesNum
NotesNum = 0 ;
def breadth_first_search(problem):
    # Start from first node of the problem Tree
    node = Node(problem.initial)
    # Check if current node meets Goal_Test criteria
    if problem.goal_test(node.state):
        return node
    # Create a Queue to store all nodes of a particular level. Import QueueClass()
    frontier=queue.Queue()
    frontier.put(node)

    # Loop until all nodes are explored(frontier queue is empty) or Goal_Test criteria are met
    while not frontier.empty():
        # Remove from frontier, for analysis
        node = frontier.get()
        # Loop over all children of the current node
        # Note: We consider the fact that a node can have multiple child nodes here
        for child in node.expand(problem):
            # If child node meets Goal_Test criteria
            if problem.goal_test(child.state):
                return child
            # Add every new child to the frontier
            frontier.put(child)
            global NotesNum
            NotesNum = NotesNum + 1
    return None
