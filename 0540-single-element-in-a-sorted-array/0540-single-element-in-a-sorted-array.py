class Solution(object):
    def singleNonDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for i in range(0,len(arr)-1,2):
            if arr[i] != arr[i+1]:
                return arr[i]
        return arr[-1]
        """
        low = 0
        high = len(arr)-1
        while low < high:
            mid = ( low + high ) // 2

            if mid % 2 == 1:
                mid -= 1
            if arr[mid] == arr[mid+1]:
                low = mid+2
            else:
                high = mid
        return arr[low]
