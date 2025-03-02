class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]
        gcd = 0
        for i in range(1,min_val+1):
            if min_val % i == 0 and max_val % i == 0:
                gcd = i
        return gcd