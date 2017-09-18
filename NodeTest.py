'''
@author William Ray Johnson
9/17/17
'''

import unittest

import Node

class NodeTest(unittest.TestCase):
    
    def setUp(self):
        self.node = Node.Node()
    
    def testCalcNodeValue(self):
        expectedValue = .5933
        actaulValue = self.node.calcNodeValue()
        
        self.assertEqual(actaulValue, expectedValue)
     
    
if __name__ == '__main__':
    unittest.main()