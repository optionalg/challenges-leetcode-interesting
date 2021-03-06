# Leetcode: Two Sum II - Input array is sorted     :BLOG:Hard:


---

Modified version of Two Sum problem  

---

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.  

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.  

You may assume that each input would have exactly one solution and you may not use the same element twice.  

Input: numbers={2, 7, 11, 15}, target=9  

Output: index1=1, index2=2  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/two-sum-ii-input-array-is-sorted)  

Credits To: [Leetcode.com](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)  

Hint: Time O(n), Space O(1). Moore voting  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: two pointers. 1. From left to right. 2. From right to left
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def twoSum(self, numbers, target):
            """
            :type numbers: List[int]
            :type target: int
            :rtype: List[int]
            """
            index1 = 0
            index2 = len(numbers) -1
            has_matched = False
            while index1 < index2:
                sum_value = numbers[index1] + numbers[index2]
                if sum_value == target:
                    has_matched = True
                    break
                elif sum_value > target:
                    index2 -= 1
                else:
                    index1 += 1
    
            if has_matched is True:
                return [index1+1, index2+1]
            else:
                return [None, None]