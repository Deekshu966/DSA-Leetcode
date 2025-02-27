class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0  # Maximum subarray sum
        min_sum = 0  # Minimum subarray sum
        cur_max = 0  # Current sum for max subarray
        cur_min = 0  # Current sum for min subarray

        for num in nums:
            cur_max = max(num, cur_max + num)  # Kadane's Algorithm for max sum
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(num, cur_min + num)  # Kadane's Algorithm for min sum
            min_sum = min(min_sum, cur_min)

        return max(abs(max_sum), abs(min_sum))
