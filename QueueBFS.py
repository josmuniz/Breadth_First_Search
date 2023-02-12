'''
@author: Devangini Patel
'''

from collections import deque


def performQueueBFS():
    """
    This function performs BFS search using a queue
    """
    #create queue
    queue = deque([]) 
    #since it is a graph, we create visited list
    visited = [] 
    #create root node
    initialState = State()
    root = Node(initialState)
    #add to queue and visited list
    queue.append(root)    
    visited.append(root.state.name)
    # check if there is something in queue to dequeue
    while len(queue) > 0:
        
        #get first item in queue
        currentNode = queue.popleft()
        
        print (("-- dequeue --"), currentNode.state.name)
        
        #check if this is goal state
        if currentNode.state.checkGoalState():
            print ("reached goal state")
            #print the path
            print ("----------------------")
            print ("Path")
            currentNode.printPath()
            break           
        #get the child nodes 
        childStates = currentNode.state.successorFunction()
        for childState in childStates:
            
            childNode = Node(State(childState))
            
            #check if node is not visited
            if childNode.state.name not in visited:
                
                #add this node to visited nodes
                visited.append(childNode.state.name)
                
                
                #add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)                        
    #print tree
    print ("----------------------")
    print ("Tree")
    root.printTree()

connections = {}
connections["Saa"] = {"daa"}
connections["daa"] = {"eaa"}
connections["eaa"] = {"haa", "raa"}
connections["haa"] = {"paa", "qaa"}
connections["faa"] = {"caa", "Gaa"}
connections["eaa"] = {"haa", "raa"}
connections["haa"] = {"paa"}
connections["paa"] = {"qaa"}
connections["raa"] = {"faa"}
connections["paa"] = {"qaa"}
connections["paa"] = {"qaa"}
connections["raa"] = {"faa"}
connections["qaa"] = {"qaa"}

'''
connections = {}
connections["Dev"] = {"Ali", "Tom"}
connections["Ali"] = {"Dev", "Seth", "Ram"}
connections["Seth"] = {"Ali", "Tom", "Harry"}
connections["Tom"] = {"Dev", "Seth", "Kai", 'Jill'}
connections["Ram"] = {"Ali", "Jill"}
connections["Kai"] = {"Tom"}
connections["Mary"] = {"Jill"}
connections["Harry"] = {"Seth"}
connections["Jill"] = {"Ram", "Tom", "Mary"}
'''

class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, name = None):
        if name == None:
            #create initial state
            self.name = self.getInitialState()
        else:
            self.name = name
    
    def getInitialState(self):
        """
        This method returns me.
        """
        initialState = "Saa"
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It finds all the persons connected to the
        current person
        """
        return connections[self.name]
        
        
    def checkGoalState(self):
        """
        This method checks whether the person is Jill.
        """ 
        #check if the person's name is Jill
        return self.name == "Gaa"
    
class Node:
    '''
    This class represents a node in the search tree
    '''
    
    def __init__(self, state):
        """
        Constructor
        """
        self.state = state
        self.depth = 0
        self.children = []
        self.parent = None
        
        
    def addChild(self, childNode):
        """
        This method adds a node under another node
        """
        self.children.append(childNode)
        childNode.parent = self
        childNode.depth = self.depth + 1
        
    
    def printTree(self):
        """
        This method prints the tree
        """
        print (self.depth , " - " , self.state.name)
        for child in self.children:
            child.printTree()
 
    
    def printPath(self):
        """
        This method prints the path from initial state to goal state
        """
        if self.parent != None:
            self.parent.printPath()
        print ("-> ", self.state.name)    
    
    
    
performQueueBFS()
