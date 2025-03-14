class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:  # If total candies are less than k, return 0
            return 0

        left, right = 1, max(candies)  # Binary search range
        result = 0

        def canDistribute(mid):
            """Helper function to check if we can give `mid` candies to `k` children"""
            count = sum(c // mid for c in candies)  # Count children that can be served
            return count >= k

        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                result = mid  # Update the result
                left = mid + 1  # Try for a larger value
            else:
                right = mid - 1  # Try for a smaller value

        return result
