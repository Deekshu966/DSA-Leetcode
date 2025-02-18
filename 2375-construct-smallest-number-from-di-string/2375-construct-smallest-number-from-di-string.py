class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        res , stack = [], []
        for i  in range(len(pattern) + 1):
            stack.append(i + 1)
            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
        return "".join(res)





















        res