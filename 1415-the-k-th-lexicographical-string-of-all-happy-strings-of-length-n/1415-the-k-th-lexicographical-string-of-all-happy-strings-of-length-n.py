class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from itertools import product

        def is_happy_string(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))

        all_combinations = [''.join(p) for p in product('abc', repeat=n)]
        happy_strings = [s for s in all_combinations if is_happy_string(s)]
        happy_strings.sort()

        return happy_strings[k - 1] if k <= len(happy_strings) else ""

