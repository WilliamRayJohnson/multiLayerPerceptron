'''
@author William Ray Johnson
9/17/17
'''

import unittest

import Net
import Node

class NetTest(unittest.TestCase):
    
    defaultNet = Net.Net(0, 0, 0)
    
    def testNetInitialization(self):
        net = Net.Net(1, 2, 1)
        
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
        nodeOne = Node.Node()
        nodeTwo = Node.Node()
        
        self.defaultNet.makeConnections([nodeOne], [nodeTwo])
        
        self.assertEqual(nodeOne.outNodes[0], nodeTwo)
        self.assertEqual(nodeTwo.inNodes[0], nodeOne)
        
    
if __name__ == '__main__':
    unittest.main()