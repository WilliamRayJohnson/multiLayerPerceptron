import Node

class Net():
    def __init__(self, numOfInput, numOfHidden, numOfOutput):
        self.inputLayer = self.initializeNodes(numOfInput)
        self.hiddenLayer = self.initializeNodes(numOfHidden)
        self.outputLayer = self.initializeNodes(numOfOutput)
        
        self.makeConnections(self.inputLayer, self.hiddenLayer)
        self.makeConnections(self.hiddenLayer, self.outputLayer)
        
        
    def initializeNodes(self, numOfNodes):
        nodes = []
        
        for node in range(numOfNodes):
            nodes.append(Node.Node(node))
            
        return nodes
        
    def makeConnections(self, leftLayer, rightLayer):
        for leftNode in leftLayer:
            for rightNode in rightLayer:
                leftNode.outNodes.append(rightNode)
                rightNode.inNodes.append(leftNode)
        