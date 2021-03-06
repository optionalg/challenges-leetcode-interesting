# Leetcode: Binary Tree Tilt     :BLOG:Medium:


---

Tree operations  

---

Given a binary tree, return the tilt of the whole tree.  

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.  

The tilt of the whole tree is defined as the sum of all nodes' tilt.  

    Example:
    Input: 
             1
           /   \
          2     3
    Output: 1
    Explanation: 
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1

Note:  

The sum of node values in any subtree won't exceed the range of 32-bit integer.  
All the tilt values won't exceed the range of 32-bit integer.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-tree-tilt)  

Credits To: [Leetcode.com](https://leetcode.com/problems/binary-tree-tilt/description/)  

Leave me comments, if you know how to solve.  

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findTilt(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            ## Idea: 
            ## Complexity: Time O(n), Space O(h)
            (_sum, cur_tilt) = self._findTilt(root)
            return cur_tilt
    
        def _findTilt(self, root):
            """
            :rtype: (sum, tilt)
            """
            if root is None:
                return (0, 0)
            if root.left is None and root.right is None:
                return (root.val, 0)
            cur_sum, cur_tilt = 0, 0
            left_sum, left_tilt = 0, 0
            right_sum, right_tilt = 0, 0
            if root.left:
                (left_sum, left_tilt) = self._findTilt(root.left)
            if root.right:
                (right_sum, right_tilt) = self._findTilt(root.right)
            cur_sum = left_sum + right_sum + root.val
            cur_tilt = left_tilt + right_tilt + abs(left_sum-right_sum)
            return (cur_sum, cur_tilt)