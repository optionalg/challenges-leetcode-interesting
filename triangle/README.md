# Leetcode: Triangle     :BLOG:Matrix:


---

Tower calculation.  

---

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.  

For example, given the following triangle  

    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).  

Credits To: [Leetcode.com](https://leetcode.com/problems/triangle/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def minimumTotal(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            ## Idea: From bottom to top.
            ##       a + b + c ... + e
            ##       To get the mininum sum, e always have 2 possibilites.
            ##       And we need to choose the smaller one
            ##       last_mininum_list: mininum total from current layer to the bottom
            ##       Notice: use space of existing array
            ##
            ## Complexity: Time O(n*n), Space O(1)
            ## Sample Data
            ##         -1
            ##        2  3
            ##      1  -1  -3
            ##
            ##          1
            ##        2   3
            if len(triangle) == 0:
                return None
            if len(triangle) == 1:
                return triangle[0][0]
    
            for j in xrange(len(triangle[-1])-1):
                triangle[-1][j] = min(triangle[-1][j], triangle[-1][j+1])
    
            for i in range(len(triangle)-2, 0, -1):
                for j in xrange(len(triangle[i])-1):
                    triangle[i][j] = min(triangle[i][j]+triangle[i+1][j], \
                                         triangle[i][j+1]+triangle[i+1][j+1])
            return triangle[0][0]+triangle[1][0]
    
        def minimumTotal_v1(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            ## Idea: From bottom to top.
            ##       a + b + c ... + e
            ##       To get the mininum sum, e always have 2 possibilites.
            ##       And we need to choose the smaller one
            ##       last_mininum_list: mininum total from current layer to the bottom
            ## Complexity: Time O(n*n), Space O(n)
            ## Sample Data
            ##         -1
            ##        2  3
            ##      1  -1  -3
            if len(triangle) == 0:
                return None
            if len(triangle) == 1:
                return triangle[0][0]
    
            last_mininum_list = [0]*len(triangle[-1])
            for i in range(len(triangle)-1, 0, -1):
                entry = triangle[i]
                for j in range(0, len(entry)-1):
                    last_mininum_list[j] = min(entry[j]+last_mininum_list[j], \
                                                entry[j+1]+last_mininum_list[j+1])
            return last_mininum_list[0] + triangle[0][0]

More Reading:  
-   [Leetcode: Valid Triangle Number](http://brain.dennyzhang.com/triangle-number/)