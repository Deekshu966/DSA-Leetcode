class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        res = []
        for i in range(n):
            # Flip the i-th character of the i-th string
            res.append('1' if nums[i][i] == '0' else '0')
        return ''.join(res)