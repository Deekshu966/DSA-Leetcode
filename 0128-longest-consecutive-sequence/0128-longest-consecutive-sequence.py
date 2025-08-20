class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1
                curr = num

                while curr + 1 in nums_set:
                    streak += 1
                    curr += 1

                    longest = max(longest, streak)
        return longest
