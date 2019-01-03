#given a binary tree, check if its a binary search tree or binary tree

class Node:

    def __init__(self,val=None):

        self.left = None

        self.right = None

        self.val = val

        

Infinity = float("inf")

NegInfinity = float("-inf")

def isBst(tree,minVal=NegInfinity, maxVal=Infinity):

    if tree is None:

        return True

    if not minVal <= tree.val <= maxVal:

        return False

    

    return isBst(tree.left,minVal,tree.val) and isBst(tree.right,tree.val,maxVal)

