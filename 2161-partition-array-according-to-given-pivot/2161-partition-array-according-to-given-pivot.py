class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        small_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = []
        result =[]
        for num in nums:
            if num < pivot:
                small_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)
        result = small_than_pivot + equal_to_pivot + greater_than_pivot
        return result