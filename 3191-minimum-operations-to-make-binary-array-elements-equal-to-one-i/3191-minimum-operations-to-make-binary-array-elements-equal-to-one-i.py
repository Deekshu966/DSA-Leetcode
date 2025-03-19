class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        operations = 0

        for i in range(n - 2):  # Ensure we have at least 3 elements to flip
            if nums[i] == 0:  # If current element is 0, we must flip
                # Flip current and next two elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1

        # If there are any remaining 0s, return -1
        if 0 in nums:
            return -1

        return operations
