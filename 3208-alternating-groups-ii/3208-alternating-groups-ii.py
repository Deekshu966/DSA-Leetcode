class Solution(object):
    def alternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        colors += colors[:k-1]  # Extend the array for circular checking
        count = 0
        valid = True  # To check if the current window is alternating
        
        # Check the first window
        for i in range(1, k):
            if colors[i] == colors[i - 1]:  # If two consecutive tiles are same, it's invalid
                valid = False
                break
        if valid:
            count += 1
        
        # Sliding window approach
        for i in range(1, n):
            if colors[i + k - 1] == colors[i + k - 2]:  # New tile breaks alternation
                valid = False
            if colors[i] == colors[i - 1]:  # Old tile leaving might restore alternation
                valid = True
                for j in range(i, i + k - 1):
                    if colors[j] == colors[j + 1]:
                        valid = False
                        break
            if valid:
                count += 1

        return count
