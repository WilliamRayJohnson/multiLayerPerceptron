import Node

class Net():
    def __init__(self, numOfInput, numOfHidden, numOfOutput):
        self.inputLayer = self.initializeNodes(numOfInput)
        self.hiddenLayer = self.initializeNodes(numOfHidden)
        self.outputLayer = self.initializeNodes(numOfOutput)
        
        self.makeConnections(self.inputLayer, self.hiddenLayer)
        self.makeConnections(self.hiddenLayer, self.outputLayer)
        
        self.totalError = 0.0
        
        
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
            leftNode.generateWeights()
        
    def calcForwardPass(self, inputValues):
        for inputNode in range(len(self.inputLayer)):
            self.inputLayer[inputNode].value = inputValues[inputNode]
            
        for hiddenNode in self.hiddenLayer:
            hiddenNode.calcNodeValue()
            
        for outputNode in self.outputLayer:
            outputNode.calcNodeValue()
            
    def calcError(self, targets):
        error = 0.0
        for outputNode in range(len(self.outputLayer)):
            error += ((targets[outputNode] - self.outputLayer[outputNode].value)**2)/2
            
        self.totalError = error
        
    def calcSensitivity(self, targets):
        for outputNode in range(len(self.outputLayer)):
            outNode = self.outputLayer[outputNode]
            for inNode in outNode.inNodes:
                sensitivity = (-(targets[outputNode] - outNode.value) *
                    outNode.value*(1 - outNode.value) * inNode.value)
                inNode.sensitivities[outputNode] = sensitivity