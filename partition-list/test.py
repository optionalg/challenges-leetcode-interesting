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
##     https://leetcode.com/problems/partition-list/description/
##    ,-----------
##    | Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
##    | 
##    | You should preserve the original relative order of the nodes in each of the two partitions.
##    | 
##    | For example,
##    | Given 1->4->3->2->5->2 and x = 3,
##    | return 1->2->2->4->3->5.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ## Basic Idea: 3 pointer. 
        ##     p_last_less: last node which is less than x
        ##     p_last_greater: last node which is greater than x
        ##     p: trasverse the list
        ## Complexity: Time O(n), Space O(1)
        ## Assumptions:

        dummy_less = ListNode(None)
        dummy_less.next = None
        
        dummy_greater = ListNode(None)
        dummy_greater.next = None

        p, p_last_less, p_last_greater = head, dummy_less, dummy_greater
        while p:
            if p.val < x:
                p_last_less.next = p
                p_last_less = p_last_less.next
            else:
                p_last_greater.next = p
                p_last_greater = p_last_greater.next
            p = p.next

        # end the list
        if p_last_less:
            p_last_less.next = None
        if p_last_greater:
            p_last_greater.next = None

        if p_last_less:
            p_last_less.next = dummy_greater.next
            return dummy_less.next
        else:
            return dummy_greater.next
