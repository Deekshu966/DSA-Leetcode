class Solution(object):
    def minCapability(self, nums, k):
        def canRob(mid):
            """Returns True if we can rob at least k houses with max <= mid."""
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= mid:  # Select this house if it's within capability
                    count += 1
                    i += 1  # Skip next house (non-adjacent condition)
                i += 1  # Move to next house
            return count >= k

        # Binary search for the minimum capability
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):  
                right = mid  # Try to minimize capability
            else:
                left = mid + 1  # Increase capability

        return left
