# Leetcode: Guess Number Higher or Lower II     :BLOG:Amusing:


---

Guess Number Higher or Lower  

---

We are playing the Guess Game. The game is as follows:  

I pick a number from 1 to n. You have to guess which number I picked.  

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.  

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.  

Example:  

    n = 10, I pick 8.
    
    First round:  You guess 5, I tell you that it's higher. You pay $5.
    Second round: You guess 7, I tell you that it's higher. You pay $7.
    Third round:  You guess 9, I tell you that it's lower. You pay $9.
    
    Game over. 8 is the number I picked.
    
    You end up paying $5 + $7 + $9 = $21.

Given a particular n >= 1, find out how much money you need to have to guarantee a win.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/guess-number-higher-or-lower-ii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: binary search
    ##      1 1 1 0 -1 -1 -1
    ## Complexity: Time O(log(n)), Space O(1)
    
    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
    # def guess(num):
    
    class Solution(object):
        def guessNumber(self, n):
            """
            :type n: int
            :rtype: int
            """
            left, right = 1, n
            while left <= right:
                mid = left + (right-left)/2
                v = guess(mid)
                if v == 0:
                    return mid
                elif v == 1:
                    left = mid + 1
                else:
                    right = mid - 1
    
            return None