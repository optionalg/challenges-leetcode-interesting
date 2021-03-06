# Leetcode: Min Stack     :BLOG:Medium:


---

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.  

---

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.  

-   push(x) -- Push element x onto stack.
-   pop() -- Removes the element on top of the stack.
-   top() -- Get the top element.
-   getMin() -- Retrieve the minimum element in the stack.

    Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/min-stack)  

Credits To: [Leetcode.com](https://leetcode.com/problems/min-stack/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: List with elements of (value, min_value)
    ##    -2 0 -3  4
    ##    linked list:
    ##     (-2, -2), (0, -2), (-3, -3), (4, -3)
    ##
    ##    length: element count
    ## Complexity:  Time: O(1), Space: O(n)
    class MinStack(object):
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.length = 0
            self.min_value = None
            self.values = 
    
    
        def push(self, x):
            """
            :type x: int
            :rtype: void
            """
            if self.length == 0:
                element = (x, x)
                self.min_value = x
            else:
                if x > self.min_value:
                    element = (x, self.min_value)
                else:
                    self.min_value = x
                    element = (x, x)
            self.values.append(element)
            self.length += 1
    
        def pop(self):
            """
            :rtype: void
            """
            if self.length == 0:
                return
    
            if self.length == 1:
                self.min_value = None
            else:
                (x, previous_min_value) = self.values[-2]
                self.min_value = previous_min_value
    
            self.values.pop()
            self.length -= 1
    
        def top(self):
            """
            :rtype: int
            """
            if len(self.values) == 0:
                return None
            else:
                (x, _min_value) = self.values[-1]
                return x
    
        def getMin(self):
            """
            :rtype: int
            """
            return self.min_value