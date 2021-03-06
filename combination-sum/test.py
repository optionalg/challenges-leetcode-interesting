#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/combination-sum/description/
##    ,-----------
##    | Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
##    | 
##    | The same repeated number may be chosen from C unlimited number of times.
##    | 
##    | Note:
##    | All numbers (including target) will be positive integers.
##    | The solution set must not contain duplicate combinations.
##    | For example, given candidate set [2, 3, 6, 7] and target 7, 
##    | A solution set is: 
##    | [
##    |   [7],
##    |   [2, 2, 3]
##    | ]
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-25 18:27:45>
##-------------------------------------------------------------------
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ## Idea:
        ## Complexity:
        ## 2 3 6 7, t=7
        ## v
        ## t/v, t/v - 1, t/v - 2, ...
        candidates = sorted(candidates)
        length = len(candidates)
        if length == 0:
            return []
        ret = []
        value = candidates[0]
        # print("target: %d, value: %d" % (target, value))
        for i in range(0, target/value+1):
            # print("here1 target: %d, value: %d, i: %d" % (target, value, i))
            if (target > i*value) and (length >= 2):
                # print("here2 target: %d, value: %d, i: %d" % (target, value, i))
                l1 = [value]*i
                l2 = self.combinationSum(candidates[1:], target - i*value)
                for item2 in l2:
                    ret.append(l1 + item2)
            else:
                if target == i*value:
                    ret.append([value]*i)
        return ret
