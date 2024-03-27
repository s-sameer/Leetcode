'''
Given a binary tree, determine if it is height-balanced. 
A tree is balanced if the difference between the heights of the left and right subtree is not more than 1 for every node
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            # get the height of left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)
            # compute the diff
            balanced = (left[0] and right[0] and abs(left[1]-right[1])<=1)
            return [balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]

        # Alternative solution
        ans = True
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            ans = abs(l-r) <= 1
            if ans != True:
                return 0
            return 1+max(l,r)
        
        dfs(root)
        return ans