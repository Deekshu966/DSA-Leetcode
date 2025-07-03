class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        store = { ")" : "(" , "}" : "{" , "]" : "[" }
        for i in s:
            if i in store:
                if stack and stack[-1] == store[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False      