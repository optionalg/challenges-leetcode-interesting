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
##     https://leetcode.com/problems/base-7/description/
##    ,-----------
##    | Given an integer, return its base 7 string representation.
##    | 
##    | Example 1:
##    | Input: 100
##    | Output: "202"
##    | Example 2:
##    | Input: -7
##    | Output: "-10"
##    | Note: The input will be in range of [-1e7, 1e7].
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ## Idea:
        ## Complexity:
        if num == 0:
            return "0"

        is_positive = True
        if num < 0:
            is_positive = False
            num = -num

        res = ""
        while num != 0:
            res = "%s%s" % (str(num % 7), res)
            num = num/7
        return res if is_positive else "-" + res
