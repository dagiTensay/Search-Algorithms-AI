class Graph:
    """
    Graph class that defines a graph data structure
    """
    def __init__(self):
        self.graph = {}
    
    def createNode(self, node):
        """
        Create a node in the graph
        """
        self.graph[node] = []
    
    def insertEdge(self, node_A, node_B, cost):
        """
        Insert Edge between node_A and node_B
        """

        if not node_A in self.graph:
            self.createNode(node_A)
        if not node_B in self.graph:
            self.createNode(node_B)
        
        self.graph[node_A].append((node_B, cost))
        self.graph[node_B].append((node_A, cost))
    
    def deleteEdge(self, node_A, node_B, cost):
        """
        delete edge between node node_A and node_B
        """
        self.graph[node_A].remove((node_B, cost))
        self.graph[node_B].remove((node_A, cost))

    def deleteNode(self, node_A):
        """
        delete node from graph
        """
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor[0] == node_A:
                    self.graph[node].remove(neighbor)
        
        del self.graph[node_A]

    def getChilds(self, node_A):
        children = []
        for tuple in self.graph[node_A]:
            children.append(tuple[0])
        return children   

