import copy
import random

import Node

class Net():
    def __init__(self, numOfInput, numOfHidden, numOfOutput, learningRate):
        self.inputLayer = self.initializeNodes(numOfInput)
        self.hiddenLayer = self.initializeNodes(numOfHidden)
        self.outputLayer = self.initializeNodes(numOfOutput)
        
        self.makeConnections(self.inputLayer, self.hiddenLayer)
        self.makeConnections(self.hiddenLayer, self.outputLayer)
        
        self.learningRate = learningRate
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
        totalError = 0.0
        for outputNode in range(len(self.outputLayer)):
            error = ((targets[outputNode] - self.outputLayer[outputNode].value)**2)/2
            self.outputLayer[outputNode].error = error
            totalError += error
            
        self.totalError = totalError
        
    def calcSensitivity(self, targets):
        for outputNode in range(len(self.outputLayer)):
            outNode = self.outputLayer[outputNode]
            for inNode in outNode.inNodes:
                sensitivity = (-(targets[outputNode] - outNode.value) *
                    outNode.value*(1 - outNode.value) * inNode.value)
                inNode.sensitivities[outputNode] = sensitivity
                
        for hiddenNode in range(len(self.hiddenLayer)):
            hidNode = self.hiddenLayer[hiddenNode]
            for inNode in hidNode.inNodes:
                dirvEtotalHNode = 0.0
                for outputNode in self.outputLayer:
                    dirvEtotalHNode += outputNode.error*(1-outputNode.error) * hidNode.value
                sensitivity = (dirvEtotalHNode * hidNode.value*(1-hidNode.value) * inNode.value)
                inNode.sensitivities[hiddenNode] = sensitivity
                
    def updateWeights(self):
        for hiddenNode in self.hiddenLayer:
            for weight in range(len(hiddenNode.weights)):
                hiddenNode.weights[weight] = (hiddenNode.weights[weight] - 
                    self.learningRate * hiddenNode.sensitivities[weight])
                    
        for inputNode in self.inputLayer:
            for weight in range(len(inputNode.weights)):
                inputNode.weights[weight] = (inputNode.weights[weight] - 
                    self.learningRate * inputNode.sensitivities[weight])
                    
    def train(self, trainingData):
        trainingDataCopy = copy.deepycopy(trainingData)
        for iter in range(1000):
            print("Interation ", iter, ":") 
            for dataPair in trainingDataCopy:
                self.calcForwardPass(dataPair[0])
                self.calcError(dataPair[1])
                print("    Error: ", self.error)
                self.calcSensitivity(dataPair[1])
                self.updateWeights()
                
            random.shuffle(trainingDataCopy)
                
                    