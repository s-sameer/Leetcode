'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        Searching all possible combinations for a specific solution -> backtracking
        """
        def traverseAll(root, curSum):
            if root is None:
                return False
            curSum += root.val
            # if at leaf node, check sum of array with target
            if root.left is None and root.right is None:
                if curSum == targetSum:
                    return True
                else:
                    return False
            return traverseAll(root.left, curSum) or traverseAll(root.right, curSum)        
        
        return traverseAll(root, 0)
        