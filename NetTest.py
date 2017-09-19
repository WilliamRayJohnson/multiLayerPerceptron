'''
@author William Ray Johnson
9/17/17
'''

import unittest

import Net
import Node

class NetTest(unittest.TestCase):
    
    defaultNet = Net.Net(0, 0, 0, 0.5)
    
    def setUpExampleNet(self):
        net = Net.Net(2, 2, 2, 0.5)
        net.inputLayer[0].weights = [0.15, 0.25]
        net.inputLayer[1].weights = [0.20, 0.30]
        net.hiddenLayer[0].weights = [0.40, 0.50]
        net.hiddenLayer[0].bias = 0.35
        net.hiddenLayer[1].weights = [0.45, 0.55]
        net.hiddenLayer[1].bias = 0.35
        net.outputLayer[0].bias = 0.60
        net.outputLayer[1].bias = 0.60
        
        return net
    
    def testNetInitialization(self):
        net = Net.Net(1, 2, 1, 0.5)
        
        inNodeOne = net.inputLayer[0]
        hiddenNodeOne = net.hiddenLayer[0]
        hiddenNodeTwo = net.hiddenLayer[1]
        outNodeOne = net.outputLayer[0]
        
        self.assertEqual(inNodeOne.inNodes, [])
        self.assertEqual(inNodeOne.outNodes[0], hiddenNodeOne)
        self.assertEqual(inNodeOne.outNodes[1], hiddenNodeTwo)
        
        self.assertEqual(hiddenNodeOne.inNodes[0], inNodeOne)
        self.assertEqual(hiddenNodeTwo.inNodes[0], inNodeOne)
        self.assertEqual(hiddenNodeOne.outNodes[0], outNodeOne)
        self.assertEqual(hiddenNodeTwo.outNodes[0], outNodeOne)
        
        self.assertEqual(outNodeOne.inNodes[0], hiddenNodeOne)
        self.assertEqual(outNodeOne.inNodes[1], hiddenNodeTwo)
        self.assertEqual(outNodeOne.outNodes, [])
        
    def testMakeConnections(self):
        nodeOne = Node.Node(0)
        nodeTwo = Node.Node(0)
        
        self.defaultNet.makeConnections([nodeOne], [nodeTwo])
        
        self.assertEqual(nodeOne.outNodes[0], nodeTwo)
        self.assertEqual(nodeTwo.inNodes[0], nodeOne)
        
    def testCalcForwardPass(self):
        net = self.setUpExampleNet()
        
        net.calcForwardPass([0.05, 0.10])
        
        x1Value = net.inputLayer[0].value
        x2Value = net.inputLayer[1].value
        h1Value = net.hiddenLayer[0].value
        h2Value = net.hiddenLayer[1].value
        y1Value = net.outputLayer[0].value
        y2Value = net.outputLayer[1].value
        
        self.assertEqual(x1Value, 0.05)
        self.assertEqual(x2Value, 0.10)
        self.assertEqual(round(h1Value, 4), 0.5933)
        self.assertEqual(round(h2Value, 4), 0.5969)
        self.assertEqual(round(y1Value, 4), 0.7514)
        self.assertEqual(round(y2Value, 4), 0.7729)
        
    def testCalcError(self):
        net = self.setUpExampleNet()
        net.calcForwardPass([0.05, 0.10])
        
        net.calcError([0.01, 0.99])
        
        expectedTotalError = 0.2984
        actualTotalError = net.totalError
        
        self.assertEqual(round(actualTotalError, 4), expectedTotalError)
        
    def testCalcSensitivity(self):
        net = self.setUpExampleNet()
        net.calcForwardPass([0.05, 0.10])
        net.calcError([0.01, 0.99])
        
        net.calcSensitivity([0.01, 0.99])
        
        w5Sensitivity = net.hiddenLayer[0].sensitivities[0]
        
        self.assertEqual(round(w5Sensitivity, 4), 0.0822)
        
    def testUpdateWeights(self):
        net = self.setUpExampleNet()
        net.calcForwardPass([0.05, 0.10])
        net.calcError([0.01, 0.99])
        net.calcSensitivity([0.01, 0.99])
        
        net.updateWeights()
    
    
if __name__ == '__main__':
    unittest.main()