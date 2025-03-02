class Solution(object):
    def countDigits(self, nums):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        n = str(nums)
        for i in n:
            digit = int(i)
            if nums %  digit == 0 and nums != 0:
                count += 1
        return count
        