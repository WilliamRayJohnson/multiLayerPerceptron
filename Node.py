'''
@author William Ray Johnson
9/17/17
'''

import random
import math

class Node():
    
    def __init__(self, nodeIndex):
        self.nodeIndex = nodeIndex
        self.value = 0
        self.bias = 0
        self.inNodes = []
        self.outNodes = []
        self.weights = []
    
    def generateWeights(self):
        for outputNode in self.outNodes:
            self.weights.append(random.random())
            
    def setValue(self, value):
        self.value = value
    
    def calcNodeValue(self):
        sum = 0.0
        for node in self.inNodes:
            sum += node.value * node.weights[self.nodeIndex]
        sum += self.bias
        
        self.value = 1/(1 + math.exp(-sum))