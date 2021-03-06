# Leetcode: Repeated String Match     :BLOG:Medium:


---

Repeated String Match  

---

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.  

For example, with A = "abcd" and B = "cdabcdab".  

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").  

Note:  
The length of A and B will be between 1 and 10000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/repeated-string-match)  

Credits To: [Leetcode.com](https://leetcode.com/problems/repeated-string-match/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Consider lengths of A and B are len_a, len_b
    ##              Let's say a match exists. k = len_b/len_a
    ##              Then we need to repeat A either k times, k+1 times or k+2 times
    ## Complexity:
    class Solution(object):
        def repeatedStringMatch(self, A, B):
            """
            :type A: str
            :type B: str
            :rtype: int
            """
            len_a = len(A)
            len_b = len(B)
            k = len_b/len_a
            C = A * k
            if B == C:
                return k
            if B in C + A:
                return k + 1
            if B in C + A + A:
                return k + 2
            return -1
    
    s = Solution()
    print s.repeatedStringMatch('abcd', 'cdabcdab')