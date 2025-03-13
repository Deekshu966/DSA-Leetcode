class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                neg += 1
            elif nums[i] < 0:
                pos += 1
            result = max(pos,neg)
        return result