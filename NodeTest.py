'''
@author William Ray Johnson
9/17/17
'''

import unittest

import Node

class NodeTest(unittest.TestCase):
    
    def setUp(self):
        self.h1 = Node.Node(0)
        self.h1.bias = 0.35
    
    def testCalcNodeValue(self):
        x1 = Node.Node(0)
        x1.setValue(0.05)
        x1.weights = [0.15]
        x2 = Node.Node(1)
        x2.setValue(0.10)
        x2.weights = [0.20]
        self.h1.inNodes = [x1, x2]
        
        expectedValue = .5933
        self.h1.calcNodeValue()
        actaulValue = self.h1.value
        
        self.assertEqual(round(actaulValue, 4), expectedValue)
     
    
if __name__ == '__main__':
    unittest.main()