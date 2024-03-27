'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''
# Intuition: get the length of the left and right subtree and add them to get the diameter of the tree rooted at the current node. 
# Update the diameter if it is greater than the current diameter...Always returning the max of the left and right subtree length 
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not root: 
                return 0
            # l and r are the lengths of the left and right subtrees
            l=dfs(root.left)
            r=dfs(root.right)
            # l+r is the diameter of the tree rooted at the current node
            ans=max(ans, l+r)
            return 1+max(l, r)
        
        dfs(root)
        return ans