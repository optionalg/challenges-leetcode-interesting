#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/reverse-integer/description/
##    ,-----------
##    | Reverse digits of an integer.
##    | 
##    | Example1: x = 123, return 321
##    | Example2: x = -123, return -321
##    | 
##    | click to show spoilers.
##    | 
##    | Note:
##    | The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:14>
##-------------------------------------------------------------------
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(abs(x) > (2 ** 31 - 1)):
            return 0
        y = 0
        if x == 0:
            return x

        is_negative = (x<0)

        if is_negative is True:
            x = -x

        while x != 0:
            y = y*10 + (x % 10)
            x = x/10

        if(abs(y) > (2 ** 31 - 1)):
            return 0

        if is_negative is True:
            return -y
        else:
            return y
            
if __name__ == '__main__':
    s = Solution()
    print s.reverse(0)
    print s.reverse(123)
    print s.reverse(-123)
## File: test.py ends
